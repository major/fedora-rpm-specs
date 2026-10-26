%global pypi_name pytorch-tokenizers

%global with_tests 1

Name:          python-%{pypi_name}
Version:       1.4.1
Release:       4%{?dist}
Summary:       C++ implementations for various tokenizers
License:       BSD-3-Clause AND Apache-2.0 AND MIT
URL:           https://github.com/meta-pytorch/tokenizers
Source0:       %{url}/archive/v%{version}.tar.gz#/tokenizers-%{version}.tar.gz

# https://github.com/meta-pytorch/tokenizers/pull/220
Patch1:        tokenizers-Fix-when-the-GNUInstallDirs.patch
# Needs review for upstreaming
# Use system libraries instead of bundled submodules. Upstream default is OFF
# so existing users are unaffected; distro builds set TOKENIZERS_USE_SYSTEM_LIBS=ON.
Patch2:        tokenizers-use-system-libs.patch
Patch3:        tokenizers-fix-include-of-absl.patch
Patch4:        tokenizers-fix-config-template.patch
Patch5:        tokenizers-system-libs-no-bundled-includes.patch

ExclusiveArch: aarch64 x86_64

BuildRequires: cmake
BuildRequires: gcc gcc-c++
BuildRequires: abseil-cpp-devel
BuildRequires: json-devel
BuildRequires: pcre2-devel
BuildRequires: re2-devel
BuildRequires: sentencepiece-devel
BuildRequires: pybind11-devel
BuildRequires: python3-cmake
BuildRequires: python3-setuptools
BuildRequires: python3-pybind11
BuildRequires: python3-sentencepiece
BuildRequires: python3-tiktoken
BuildRequires: python3-torch
BuildRequires: python3-tokenizers
# For check
%if 0%{?with_tests}
BuildRequires: python3-pytest
BuildRequires: python3-huggingface-hub
%endif

%global _description %{expand:
C++ implementations for various tokenizers (sentencepiece, tiktoken etc).
Useful for other PyTorch repos such as torchchat, ExecuTorch to build LLM
runners using ExecuTorch stack or AOT Inductor stack.
}

%description %_description

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %_description

%package -n     python3-%{pypi_name}-devel
Summary:        %{summary}
Requires:       python3-%{pypi_name}%{?_isa} = %{version}-%{release}
Requires:       abseil-cpp-devel
Requires:       json-devel
Requires:       pcre2-devel
Requires:       re2-devel
Requires:       sentencepiece-devel
Provides:       python3-%{pypi_name}-devel-static

%description -n python3-%{pypi_name}-devel
Development libraries and CMake bits for python3-%{pypi_name}.


%prep
%autosetup -p1 -n tokenizers-%{version}
rm -rf third-party/{sentencepiece,re2,abseil-cpp,json,pcre2}

%generate_buildrequires
%if 0%{?with_tests}
%pyproject_buildrequires -r
%else
%pyproject_buildrequires
%endif

%build
%cmake -DCMAKE_INSTALL_LIBDIR=%{_libdir} -DTOKENIZERS_USE_SYSTEM_LIBS=ON -DSUPPORT_REGEX_LOOKAHEAD=ON
%cmake_build

export CMAKE_ARGS="-DTOKENIZERS_USE_SYSTEM_LIBS=ON -DSUPPORT_REGEX_LOOKAHEAD=ON"
%pyproject_wheel

%install
%cmake_install

%pyproject_install
%pyproject_save_files pytorch_tokenizers

%if 0%{?with_tests}
%check
%pyproject_check_import
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE
%doc README.md
%exclude %{python3_sitearch}/pytorch_tokenizers/include

%files -n python3-%{pypi_name}-devel
%{python3_sitearch}/pytorch_tokenizers/include
%dir %{_includedir}/pytorch/
%{_includedir}/pytorch/tokenizers/
%{_libdir}/cmake/tokenizers/
# Used by pytorch ecosystem (eg executorch)
%{_libdir}/lib*.a

%changelog
* Fri Oct 23 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-4
- Updates and fixes for review

* Fri Oct 09 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-3
- Enable import checks, minor updates

* Wed Sep 23 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-2
- Run a full cmake build to get all binaries
- Add various devel deps
- Update for json deps

* Wed Sep 23 2026 Peter Robinson <pbrobinson@fedoraproject.org> - 1.4.1-1
- Initial package
