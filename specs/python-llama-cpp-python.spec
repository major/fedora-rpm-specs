%global pypi_name llama-cpp-python
%global pypi_version 0.3.14
# it's all python code
%global debug_package %{nil}

# Based on the commit of llama-cpp-python tagged with 0.3.14:
# https://github.com/abetlen/llama-cpp-python/releases/tag/v0.3.14
# we can see that the /vendor/llama-cpp links to the llama-cpp repository
# locked at the specific commit, which is provided as a source
%global llama_repo https://github.com/ggerganov/llama.cpp
%global llama_commit 79e0b68c178656bb0632cb8602d2940b755077f8
%global llama_archive llama.cpp-79e0b68.tar.gz

# Exclude any .so built from the bundled tarball so that the automatic 'Provides'
# does not pollute the RPM dependency database -> the regex should exclude these four libraries:
# - libggml-base.so()(64bit)
# - libggml-cpu.so()(64bit)
# - libggml.so()(64bit)
# - libllama.so()(64bit)
%global __provides_exclude_from %{python3_sitearch}/.*\.so$
%global __requires_exclude_from %{python3_sitearch}/.*\.so$

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        %autorelease
License:        MIT
Summary:        Simple Python bindings for @ggerganov's llama.cpp library
URL:            https://github.com/abetlen/llama-cpp-python
Source0:        %{url}/archive/v%{version}/%{pypi_name}-%{version}.tar.gz
Source1:        %{llama_repo}/archive/%{llama_commit}.tar.gz#/%{llama_archive}
Patch1:         0001-don-t-build-llava.patch
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

# We do not install llama-cpp-devel, since it has the unversioned libllama.so.
# Instead, we specify that by installing this package, we provide
# the bundled llama-cpp at the specific commit
Provides:       bundled(llama-cpp) = %{sub %llama_commit 1 7}

%description -n python3-%{pypi_name}
%{pypi_name} provides:
Low-level access to C API via `ctypes` interface.
High-level Python API for text completion.
OpenAI compatible web server

# Extract the contents of the specific llama-cpp tarball into the /vendor/llama.cpp within
# the python bindings directory. Since llama-cpp cmake build is allowed (patch 0001),
# the llama-cpp cmake build will also be triggered.
%prep
%autosetup -p1 -n %{pypi_name}-%{version} -Sgit
tar -xf %{SOURCE1} --strip-components=1 --directory %{_builddir}/%{pypi_name}-%{version}/vendor/llama.cpp

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

# Remove the unnecessary binaries built by llama-cpp cmake as they don't need to be packaged.
rm -rf %{buildroot}%{python3_sitearch}/bin/
rm -rf %{buildroot}%{python3_sitearch}/include/
# The following 'lib64' folder contains only some .cmake, .pc, and redundant .so files
# (the same four as listed on top of the specfile). Since the actually used .so files can be
# found within %{buildroot}%{python3_sitearch}/llama_cpp/lib64/, we can safely remove this.
rm -rf %{buildroot}%{python3_sitearch}/lib64/

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog

