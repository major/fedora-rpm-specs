Name:           python-tiktoken
Version:        0.11.0
Release:        %autorelease
Summary:        tiktoken is a fast BPE tokeniser for use with OpenAI's models
# Statically linked deps and their licenses.
# When updating, check the generated LICENSE.dependencies file.
#
# tiktoken is MIT
# (MIT OR Apache-2.0) AND Unicode-DFS-2016: bstr v1.7.0
# (MIT OR Apache-2.0) AND Unicode-DFS-2016: regex-syntax v0.8.2
# Apache-2.0 OR MIT: rustc-hash v1.1.0
# Apache-2.0: pyo3 v0.19.2
# Apache-2.0: pyo3-ffi v0.19.2
# MIT OR Apache-2.0: bit-set v0.5.3
# MIT OR Apache-2.0: bit-vec v0.6.3
# MIT OR Apache-2.0: cfg-if v1.0.0
# MIT OR Apache-2.0: libc v0.2.149
# MIT OR Apache-2.0: lock_api v0.4.10
# MIT OR Apache-2.0: parking_lot v0.12.1
# MIT OR Apache-2.0: parking_lot_core v0.9.8
# MIT OR Apache-2.0: regex v1.10.2
# MIT OR Apache-2.0: regex-automata v0.4.3
# MIT OR Apache-2.0: scopeguard v1.2.0
# MIT OR Apache-2.0: smallvec v1.11.1
# MIT OR Apache-2.0: unindent v0.1.11
# MIT: fancy-regex v0.11.0
# MIT: memoffset v0.9.0
# Unlicense OR MIT: aho-corasick v1.1.2
# Unlicense OR MIT: memchr v2.6.4
License:        MIT AND ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND Apache-2.0 AND (Apache-2.0 OR MIT) AND (Unlicense OR MIT)
URL:            https://pypi.org/project/tiktoken/
Source:         %{pypi_source tiktoken}

BuildRequires:  python3-devel
BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
tiktoken is a fast BPE tokeniser for use with OpenAI's models.}


%description %_description

%package -n     python3-tiktoken
Summary:        %{summary}

%description -n python3-tiktoken %_description


%prep
%autosetup -p1 -n tiktoken-%{version}
%cargo_prep


%generate_buildrequires
%cargo_generate_buildrequires -f python
%pyproject_buildrequires


%build
%pyproject_wheel
%{cargo_license} > LICENSE.dependencies


%install
%pyproject_install
%pyproject_save_files tiktoken tiktoken_ext


%check
%pyproject_check_import


%files -n python3-tiktoken -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE.dependencies


%changelog
%autochangelog
