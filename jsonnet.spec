Name:           jsonnet
Version:        0.19.1
Release:        2%{?dist}
Summary:        A data templating language based on JSON

# The bundled MD5 library is RSA licenced
License:        ASL 2.0 and RSA

URL:            https://github.com/google/jsonnet
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

# Downstream man pages in groff_man(7) format
Source1:        jsonnet.1
Source2:        jsonnetfmt.1

# Upstream wants to build single source wheels
# these benefit from static linking,
# but we want to link to libjsonnet here so we are sharing the lib
Patch0001:      0001-Dynamic-link-to-libjsonnet-rather-than-static.patch
# Upstream hard codes compiler flags
Patch0002:      0002-jsonnet-0.17.0-do-not-override-compiler-flags.patch
# Upstream ships rapidyaml inside this source repo
Patch0003:      0003-jsonnet-0.19.1-Use-system-provided-rapidyaml.patch


# Bundled MD5 C++ class with very permissive license (RSA)
# rpmlint must be notified of the unversioned provides
Provides:       bundled(md5-thilo)

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

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
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}

%description devel %{_description}


%package doc
Summary:        Documentation for %{name}
License:        CC-BY
BuildArch:      noarch

%description doc %{_description}


%prep
%autosetup

# use system json lib instead
rm -rfv third_party/json/*

# don't bundel rapidyaml
rm -rfv third_party/rapidyaml/*

# don't bundle thirdparty doc resources
# this leaves the doc "unbuilt" but still sorta useful
rm -rf doc/third_party
rm -rf doc/.gitignore


%build

%if 0%{?rhel} == 8
# required macro drop for EL8
%undefine __cmake_in_source_build
%endif


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
%{py3_build}


%install
%{cmake_install}

# install python binding
%{py3_install}

install -d '%{buildroot}%{_mandir}/man1'
install -t '%{buildroot}%{_mandir}/man1' -p -m 0644 '%{SOURCE1}' '%{SOURCE2}'


%check
%ctest


%files
%{_bindir}/jsonnet
%{_bindir}/jsonnetfmt
%{_mandir}/man1/jsonnet.1*
%{_mandir}/man1/jsonnetfmt.1*

%files libs
%license LICENSE
%doc README.md
%{_libdir}/lib%{name}*.so.*

%files devel
%{_includedir}/lib%{name}*
%{_libdir}/lib%{name}*.so

%files -n python3-%{name}
# rpmlint must be notified this is not versioned on purpose
%{python3_sitearch}/_%{name}*.so
%{python3_sitearch}/%{name}-%{version}-py%{python3_version}.egg-info

%files doc
%license LICENSE
%doc README.md
%doc CONTRIBUTING
%doc doc
%doc examples


%changelog
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
