%define _epel   %{?epel:%{epel}}%{!?epel:0}

Name:		fasttext
Version:	0.9.2
Release:	6%{?dist}
Summary:	Efficient learning of word representations and sentence classification

License:	MIT
URL:		https://github.com/facebookresearch/fastText
Source0:	https://github.com/facebookresearch/fastText/archive/v%{version}/%{name}-%{version}.tar.gz
# Enable to install %%{_libdir} instead of hardcoded lib directory
Patch0:		enable-install-lib64.patch
# Respect CMake CXXFLAGS set by %%cmake (Needed for hardening with -fPIC)
Patch1:		respect-cmake-cxxflags.patch

%if %{_epel} == 7
BuildRequires:	cmake3
BuildRequires:	devtoolset-7-gcc
BuildRequires:	devtoolset-7-gcc-c++
%else
BuildRequires:	cmake
BuildRequires:	gcc
BuildRequires:	gcc-c++
%endif
Requires:	%{name}-libs = %{version}-%{release}

%description
The fastText is a library for efficient learning of
word representations and sentence classification.

%package libs
Summary:	Runtime libraries for fastText

%description libs
This package contains the libraries for fastText.

%package tools
Summary:	Tools for fastText
Requires:	%{name}-libs = %{version}-%{release}

%description tools
This package contains tools for manipulate models for fastText.

%package devel
Summary:	Libraries and header files for fastText
Requires:	%{name}-libs = %{version}-%{release}

%description devel
This package contains header files to develop a software using fastText.

%prep
%autosetup -p1 -n fastText-%{version}

%build
%if %{_epel} == 7
. /opt/rh/devtoolset-7/enable
%endif
export CXXFLAGS="%build_cxxflags -fPIC"
%if %{_epel} == 7
%cmake3 .
V=1 %cmake3_build
%else
%cmake .
V=1 %cmake_build
%endif

%install
%if %{_epel} == 7
%cmake3_install
%else
%cmake_install
%endif
find %{buildroot} -name '*.a' -delete

%files 
%{_bindir}/fasttext

%ldconfig_scriptlets libs

%files libs
%license LICENSE
%doc CODE_OF_CONDUCT.md CONTRIBUTING.md README.md
%{_libdir}/libfasttext.so.0

%files devel
%dir %{_includedir}/fasttext
%{_includedir}/fasttext/
%{_libdir}/libfasttext.so
%{_libdir}/pkgconfig/fasttext.pc

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Oct 01 2020 Kentaro Hayashi <kenhys@gmail.com> - 0.9.2-1
- New upstream release

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 1 2019 Kentaro Hayashi <hayashi@clear-code.com> - 0.9.1-1
- initial packaging
