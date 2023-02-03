import streamlit as st
from non_exact_match import lcs, levenshtein_dist, tools


if __name__ == '__main__':

    st.set_page_config(page_title="Non-Exact Match Search")

    user_input = st.text_area("Escreva o padrão que deseja procurar", """Loerem Ipssum is simply""")
    print(user_input)
    user_input_2 = st.text_area("Escreva o texto alvo", """Loeem Isum is simpl dummy text of the printing and
                                                      typesetting industry. Lorem Ilpssum has been the industry's 
                                                      standard dummy text ever since the 1590s, when an unknown""")

    name_lenth = len(user_input.split(" "))
    ngram_input = tools.generate_ngrams(tools.string_normalize(user_input_2), ngram=name_lenth)
    print(ngram_input)
    left, center, right = st.columns([1, 1, 1])
    st.text("Ngrams result")
    st.text(ngram_input)

    user_input_normalized = tools.string_normalize(user_input)

    longest = 999
    longest_lcs = 0
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

    st.text(f"----------------------LCS------------------------")
    st.text(f"lcsubstring leght: {lcs_result_f}")
    st.text(f"lcsubstring match text: {text_result_f}")
    st.text(f"lcsubstring + ngram match text: {ngram_result_lcs}")
    st.text(f"leveshtein distance to real string: {err_lcs}")
    st.text(f"---------------------NGRAM-----------------------")
    st.text(f"ngram + leveshtein match text: {ngram_result}")
    st.text(f"leveshtein distance to real string: {longest}")

    if not user_input:
      st.warning("Please fill out so required fields")

