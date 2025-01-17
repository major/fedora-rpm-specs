Name:           jsonnet
Version:        0.20.0
%global so_version 0
Release:        11%{?dist}
Summary:        A data templating language based on JSON

# The entire source is Apache-2.0, except:
#   - doc/ (the HTML documentation) is doc/_layouts/base.html is CC-BY-2.5,
#     which is reflected in the License of the -doc subpackage
#   - The dependency “json” is a header-only library, so it must be treated as
#     a static library. Its license “MIT AND CC0-1.0” (the latter from a
#     bundled hedley) therefore contributes to the licenses of the binary RPMs
#     that include compiled programs and libraries.
License:        Apache-2.0 AND MIT AND CC0-1.0

URL:            https://github.com/google/jsonnet
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Downstream man pages in groff_man(7) format
Source1:        jsonnet.1
Source2:        jsonnetfmt.1

# Upstream wants to build single source wheels
# these benefit from static linking,
# but we want to link to libjsonnet here so we are sharing the lib
Patch:          0001-Dynamic-link-to-libjsonnet-rather-than-static.patch
# Upstream hard codes compiler flags
Patch:          0002-patch-CMakeLists.txt-to-stop-overriding-build-flags.patch
# Upstream ships rapidyaml inside this source repo
Patch:          0003-Use-system-provided-rapidyaml.patch
# Fix deprecated python interfaces
Patch:          0004-fix-remove-deprecated-declarations-in-python-binding.patch
# Downstream-only: backport support for rapidyaml 0.7
Patch:          0005-Downstream-only-backport-support-for-rapidyaml-0.7.patch

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
%if %{undefined fc40} && %{undefined fc41}
ExcludeArch:    %{ix86}
%endif

# Bundled MD5 C++ class in third_party/md5/ with very permissive license (RSA)
# Per current guidance, we don’t need to record this as an additional license:
# https://docs.fedoraproject.org/en-US/legal/misc/#_licensing_of_rsa_implementations_of_md5
# rpmlint must be notified of the unversioned provides
Provides:       bundled(md5-thilo)

BuildRequires:  python3-devel

BuildRequires:  bash cmake gcc gcc-c++ gtest-devel make

# json is header only, so note the static lib for tracking
BuildRequires:  json-devel json-static
BuildRequires:  rapidyaml-devel

# Set our toplevel runtime requirements
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%global _description %{expand:
A data templating language for app and tool developers based on JSON}

%description %{_description}


%package -n python3-%{name}
Summary:        %{name} Bindings for Python
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description -n python3-%{name} %{_description}


%package libs
Summary:        Shared Libraries for %{name}

%description libs %{_description}


%package devel
Summary:        Development Headers for %{name}
# This contains nothing derived from json-static, so the (MIT AND CC0-1.0)
# portion can be omitted and the license is simply:
License:        Apache-2.0

Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}


%package doc
Summary:        Documentation for %{name}
# This contains nothing derived from json-static, so the (MIT AND CC0-1.0)
# portion can be omitted. HTML documentation from doc/ is CC-BY-2.5; examples/
# are Apache-2.0.
License:        Apache-2.0 AND CC-BY-2.5
BuildArch:      noarch

%description doc %{_description}


%prep
%autosetup -p1

# use system json lib instead
rm -rfv third_party/json/*

# don't bundel rapidyaml
rm -rfv third_party/rapidyaml/*

# don't bundle thirdparty doc resources
# this leaves the doc "unbuilt" but still sorta useful
rm -rf doc/third_party
rm -rf doc/.gitignore

# The documentation and examples include a few executable shell scripts.
# Because this is an unusual location to install scripts, we need to fix their
# shebangs manually. See:
# https://docs.fedoraproject.org/en-US/packaging-guidelines/#_shebang_lines
find doc examples -type f -perm /0111 -name '*.sh' -print0 |
  xargs -r -0 -t sed -r -i '1{s@^#!/usr/bin/env[[:blank:]]+bash@#!/bin/bash@}'


%generate_buildrequires
%pyproject_buildrequires


%build
# FIXME:
# For reasons I'm not following, json-devel isn't added to include by cmake
#
# explicitly set -fPIC so python can pick it up later on
export CXXFLAGS="%{optflags} -fPIC -I%{_includedir}/nlohmann"

# setup our build environment
%cmake -DBUILD_SHARED_BINARIES:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=OFF -DUSE_SYSTEM_JSON:BOOL=ON -DUSE_SYSTEM_GTEST:BOOL=ON

# make tools and headers
%cmake_build

# make python binding
%pyproject_wheel


%install
%{cmake_install}

# install python binding
%pyproject_install
%pyproject_save_files _jsonnet

install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'


%check
%ctest

LD_LIBRARY_PATH='%{buildroot}%{_libdir}' \
    PYTHONPATH='%{buildroot}%{python3_sitearch}' \
    %{python3} python/_jsonnet_test.py


%files
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt
%{_mandir}/man1/jsonnet.1*
%{_mandir}/man1/jsonnetfmt.1*

%files libs
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}.so.%{so_version}{,.*}
%{_libdir}/lib%{name}++.so.%{so_version}{,.*}

%files devel
%{_includedir}/lib%{name}*
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}++.so

%files -n python3-%{name} -f %{pyproject_files}

%files doc
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc doc
%doc examples


%changelog
* Wed Jan 15 2025 Benjamin A. Beasley <code@musicinmybrain.net> - 0.20.0-11
- Drop i686 support (in Fedora 42 and later)

* Thu Sep 05 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.20.0-10
- Rebuilt for rapidyaml 0.7.2

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jun 07 2024 Python Maint <python-maint@redhat.com> - 0.20.0-8
- Rebuilt for Python 3.13

* Mon May 06 2024 Benjamin A. Beasley <code@musicinmybrain.net> - 0.20.0-7
- Rebuilt for rapidyaml 0.6.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jan 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Tue Jun 13 2023 Python Maint <python-maint@redhat.com> - 0.20.0-3
- Rebuilt for Python 3.12

* Thu May 25 2023 Benjamin A. Beasley <code@musicinmybrain.net> - 0.20.0-2
- Drop “RSA” license per current guidance on RSA MD5 implementations
- Drop EPEL8 conditionals from spec file
- Update License to SPDX
- Build Python bindings with pyproject-rpm-macros (“new guidelines”)
- Run the Python tests
- Do not glob over the shared library SONAME version
- Fix up shebangs in the docs and examples

* Mon Apr 17 2023 Pat Riehecky <riehecky@fnal.gov> - 0.20.0
- Update to 0.20.0

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.19.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Nov 2 2022 Pat Riehecky <riehecky@fnal.gov> - 0.19.1
- Update to 0.19.1
- v0.19.0 is not binary compatible with previous versions of libjsonnet.
- this version introduces versioned soname objects from upstream

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.17.0-5
- Rebuilt for Python 3.11

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.17.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 25 2021 Benjamin A. Beasley <code@musicinmybrain.net> - 0.17.0-2
- Add downstream man pages
- Fix Summary

* Thu Jun 17 2021 Pat Riehecky <riehecky@fnal.gov> - 0.17.0-1
- Initial package.
