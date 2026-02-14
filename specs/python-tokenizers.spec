%bcond check 1

Name:           python-tokenizers
Version:        0.22.2
Release:        %autorelease
Summary:        Implementation of today's most used tokenizers

# pyarrow and pandas are not available on i686
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

# Generated license info from Rust dependencies
### BEGIN LICENSE SUMMARY ###
# 
# (MIT OR Apache-2.0) AND Unicode-DFS-2016
# Apache-2.0
# Apache-2.0 AND MIT
# Apache-2.0 OR BSL-1.0
# Apache-2.0 OR MIT
# Apache-2.0 OR MIT OR Zlib
# BSD-2-Clause
# BSD-2-Clause OR Apache-2.0 OR MIT
# MIT
# MIT OR Apache-2.0
# Unlicense OR MIT
###  END LICENSE SUMMARY  ###

# License expression simplified by the special rule for OR expressions:
# https://docs.fedoraproject.org/en-US/legal/license-field/#_special_rules_for_or_expressions
%global license_expression %{shrink:
Unicode-DFS-2016 AND
Apache-2.0 AND
(Apache-2.0 AND MIT) AND
(Apache-2.0 OR BSL-1.0) AND
(Apache-2.0 OR MIT OR Zlib) AND
BSD-2-Clause AND
MIT AND
(Unlicense OR MIT)
}

SourceLicense:  Apache-2.0
License:        %{license_expression}
URL:            https://github.com/huggingface/tokenizers
Source:         %{pypi_source tokenizers}
# A patch I wrote, updating the sources for PyO3 0.27 support
# https://github.com/huggingface/tokenizers/pull/1941.patch
Patch:          1941.patch

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli
# For tests
BuildRequires:  python3dist(datasets)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-asyncio)
BuildRequires:  python3dist(pytest-datadir)
BuildRequires:  python3dist(pytest-xdist)


%global _description %{expand:
Provides an implementation of today's most used tokenizers,
with a focus on performance and versatility.
Bindings over the rust-tokenizers implementation.}

%description %_description

%package -n     python3-tokenizers
Summary:        %{summary}

%description -n python3-tokenizers %_description


%prep
%autosetup -p1 -n tokenizers-%{version}
%cargo_prep
# Copy out LICENSE
cp -a tokenizers/LICENSE LICENSE
# Remove vendored tokenizers
rm -r tokenizers/
# Remove locked versions
rm bindings/python/Cargo.lock
# Replace the path-based dependency on the bundled crate with an exact-version
# dependency.
tomcli set bindings/python/Cargo.toml del dependencies.tokenizers.path
tomcli set bindings/python/Cargo.toml str dependencies.tokenizers.version '=%{version}'


%generate_buildrequires
# Get the cargo buildrequires first, so that maturin will succeed
cd bindings/python/
%cargo_generate_buildrequires
cd ../../
%pyproject_buildrequires


%build
# Generate the dependency license file first, so maturin will find it
cd bindings/python/
%cargo_license_summary
%{cargo_license} > ../../LICENSE.dependencies
cd ../../
%pyproject_wheel


%install
%pyproject_install
# When saving the files, assert that a license file was found
%pyproject_save_files -l tokenizers


%check
%pyproject_check_import
cd bindings/python
# Per the Makefile, this option is required for tests to pass
%cargo_test -- --no-default-features
# only run the tests, not the benches
# the deselected tests are:
# - test_datasets fails with: "TypeError: Pickler._batch_setitems() takes 2 positional arguments but 3 were given"
# - test_gzip fails with: "FileNotFoundError: [Errno 2] No such file or directory: 'data/my-file.0.gz'"
# - the rest of the deselects are network accesses
%pytest -s -v ./tests/ \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_char_to_token" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_char_to_word" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_invalid_truncate_direction" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_n_sequences" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_sequence_ids" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_token_to_chars" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_token_to_sequence" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_token_to_word" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_truncation" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_word_to_chars" \
        --deselect="tests/bindings/test_encoding.py::TestEncoding::test_word_to_tokens" \
        --deselect="tests/bindings/test_models.py::TestBPE::test_instantiate" \
        --deselect="tests/bindings/test_models.py::TestWordLevel::test_instantiate" \
        --deselect="tests/bindings/test_models.py::TestWordPiece::test_instantiate" \
        --deselect="tests/bindings/test_processors.py::TestByteLevelProcessing::test_processing" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_async_methods_existence" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_basic_encoding" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_concurrency" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_decode" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_encode" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_error_handling" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_large_batch" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_numpy_inputs" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_performance_comparison" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_various_input_formats" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_with_special_tokens" \
        --deselect="tests/bindings/test_tokenizer.py::TestAsyncTokenizer::test_with_truncation_padding" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_decode_skip_special_tokens" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_decode_stream_fallback" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_encode_add_special_tokens" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_encode_formats" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_encode_special_tokens" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_from_pretrained" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_from_pretrained_revision" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_multiprocessing_with_parallelism" \
        --deselect="tests/bindings/test_tokenizer.py::TestTokenizer::test_splitting" \
        --deselect="tests/bindings/test_trainers.py::TestUnigram::test_continuing_prefix_trainer_mismatch" \
        --deselect="tests/bindings/test_trainers.py::TestUnigram::test_train" \
        --deselect="tests/bindings/test_trainers.py::TestUnigram::test_train_parallelism_with_custom_pretokenizer" \
        --deselect="tests/documentation/test_pipeline.py::TestPipeline::test_bert_example" \
        --deselect="tests/documentation/test_pipeline.py::TestPipeline::test_pipeline" \
        --deselect="tests/documentation/test_quicktour.py::TestQuicktour::test_quicktour" \
        --deselect="tests/documentation/test_tutorial_train_from_iterators.py::TestTrainFromIterators::test_datasets" \
        --deselect="tests/documentation/test_tutorial_train_from_iterators.py::TestTrainFromIterators::test_gzip" \
        --deselect="tests/implementations/test_bert_wordpiece.py::TestBertWordPieceTokenizer::test_basic_encode" \
        --deselect="tests/implementations/test_bert_wordpiece.py::TestBertWordPieceTokenizer::test_multiprocessing_with_parallelism" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_add_prefix_space" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_basic_encode" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_lowerspace" \
        --deselect="tests/implementations/test_byte_level_bpe.py::TestByteLevelBPE::test_multiprocessing_with_parallelism" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_basic_encode" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_decoding" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_lowercase" \
        --deselect="tests/implementations/test_char_bpe.py::TestCharBPETokenizer::test_multiprocessing_with_parallelism" \
        --deselect="tests/test_serialization.py::TestSerialization::test_full_serialization_albert" \
        --deselect="tests/test_serialization.py::TestSerialization::test_str_big"

cd ../../


%files -n python3-tokenizers -f %{pyproject_files}
%doc bindings/python/README.md bindings/python/CHANGELOG.md
%license LICENSE
%license LICENSE.dependencies


%changelog
%autochangelog
