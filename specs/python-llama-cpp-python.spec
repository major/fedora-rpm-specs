%global pypi_name llama-cpp-python
%global pypi_version 0.3.7
# it's all python code
%global debug_package %{nil}

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
License:        MIT
Summary:        Simple Python bindings for @ggerganov's llama.cpp library
URL:            https://github.com/abetlen/llama-cpp-python
Source:         %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Patch1:         0001-don-t-build-llama.cpp-and-llava.patch
Patch2:         0002-search-for-libllama-so-in-usr-lib64.patch
Patch3:         https://github.com/abetlen/llama-cpp-python/pull/1718.patch#/0003-drop-optional-dependency-of-scikit-build-core.patch

%bcond_without test

# this is what llama-cpp is on
# and this library is by default installed in /usr/lib64/python3.12/site-packages/llama_cpp/__init__.py
ExclusiveArch:  x86_64 aarch64

BuildRequires:  git-core
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  ninja-build
BuildRequires:  python3-devel
BuildRequires:  llama-cpp-devel
%if %{with test}
BuildRequires:  python3-pytest
BuildRequires:  python3-scipy
BuildRequires:  python3-huggingface-hub
%endif

%generate_buildrequires
%pyproject_buildrequires

%description
%{pypi_name} provides:
Low-level access to C API via `ctypes` interface.
High-level Python API for text completion.
OpenAI compatible web server

%package -n     python3-%{pypi_name}
Summary:        %{summary}
# -devel has the unversioned libllama.so
Requires:       llama-cpp-devel

%description -n python3-%{pypi_name}
%{pypi_name} provides:
Low-level access to C API via `ctypes` interface.
High-level Python API for text completion.
OpenAI compatible web server


%prep
%autosetup -p1 -n %{pypi_name}-%{version} -Sgit

%build
%pyproject_wheel

%if %{with test}
%check
# these 3 llama tests need ggml-vocab-llama-spm model, we'll run them in testing farm, see plans/
%pytest -v -k 'not test_llama_cpp_tokenization and not test_real_llama and not test_real_model' tests/
%endif

%install
%pyproject_install
%pyproject_save_files -l llama_cpp -L

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog

