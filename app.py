import streamlit as st
from non_exact_match import lcs, levenshtein_dist, tools


if __name__ == '__main__':

    st.set_page_config(page_title="Non-Exact Match Search", layout="wide")
    left, right = st.columns(2)
    left.title("Faça a busca de um padrão em um texto")
    right.header("Resultados")

    user_input = left.text_area("Escreva o padrão que deseja procurar", """Loerem Ipssum is simply""")
    user_input_2 = left.text_area("Escreva o texto alvo", """Loeem Isum is simpl dummy text of the printing and
                                                      typesetting industry. Lorem Ilpssum has been the industry's 
                                                      standard dummy text ever since the 1590s, when an unknown""")
    user_input_2_normalized = tools.string_normalize(user_input_2)
    user_input_normalized = tools.string_normalize(user_input)

    user_input_lenth = len(user_input.split(" "))
    ngram_input = tools.generate_ngrams(user_input_2_normalized, ngram=user_input_lenth)


    longest = 999
    longest_lcs = 0
    accepted_lcs = 85
    for ngram in ngram_input:
        err = levenshtein_dist.edit_distance(ngram, user_input_normalized)
        text_result, start, end, lcs_result = lcs.lcsubstring(user_input_normalized, ngram)
        if err < longest:
            longest = err
            ngram_result = ngram
        if lcs_result > longest_lcs:
            ngram_result_lcs = ngram
            longest_lcs = lcs_result
            text_result_f, start_f, end_f, lcs_result_f = text_result, start, end, lcs_result
            err_lcs = levenshtein_dist.edit_distance(ngram_result_lcs, user_input_normalized)

    right.text(f"----------------------LCS------------------------")
    right.text(f"lcsubstring leght: {lcs_result_f}")
    right.text(f"percentage of what the lcs found: {round((lcs_result_f / len(user_input_normalized)) * 100, 1)}%")
    right.text(f"lcsubstring match text: {text_result_f}")
    right.text(f"lcsubstring + ngram match text: {ngram_result_lcs}")
    right.text(f"leveshtein distance lcsubstring + ngram to pattern string: {err_lcs}")
    right.text(f"---------------------NGRAM-----------------------")
    right.text(f"ngram + leveshtein match text: {ngram_result}")
    right.text(f"leveshtein distance ngram string to pattern string: {longest}")
    right.text(f"---------------------IN Python-----------------------")
    right.text(f"Python string-searching: {user_input_normalized in user_input_2_normalized}")
    if not user_input:
      st.warning("Please fill out so required fields")

