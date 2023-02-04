# The tar is biosig4c++, but it also appears to include sources for python,
# matlab, and so on. Should the name be changed?

%global _description %{expand:
BioSig is a software library for processing of biomedical signals (EEG, ECG,
etc.) with Matlab, Octave, C/C++ and Python. A standalone signal viewer
supporting more than 30 different data formats is also provided.}

%global pretty_name biosig

%global commit a2aae2bb20b0f149fd70e00784f6c7b29f8294f2
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:       biosig4c++
Version:    1.9.5
Release:    10.git%{shortcommit}%{?dist}
Summary:    A software library for processing of biomedical signals

License:    GPLv3+
URL:        https://sourceforge.net/projects/%{pretty_name}/

# Fetch the snapshot---this contains code for other biosig tools also which we don't need
# git clone https://git.code.sf.net/p/biosig/code biosig-all
# cd biosig-all
# Remove symlink and replace with actual files
# rm biosig4c++/extern -f
# cp -r biosig4matlab/doc biosig4c++/extern
# tar -cvzf biosig4c++-1.9.3-94296e0ee92c39636235d390c313ad1dfe644a88.tar.gz biosig4c++/

Source0:    %{name}-%{version}-%{commit}.tar.gz
Patch0: biosig++-c99-1.patch
Patch1: biosig++-c99-2.patch

BuildRequires:  suitesparse-devel
BuildRequires:  tinyxml-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconf-pkg-config
BuildRequires:  libb64-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires: make

%description
%{_description}

%package devel
Summary:    A software library for processing of biomedical signals
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
%{_description}


%prep
%autosetup -p1 -n %{name}


%build
autoreconf -i -f
%configure
%make_build
%make_build save2gdf
%make_build biosig_fhir

# make %{?_smp_mflags} mex4o
# make %{?_smp_mflags} biosig4python


%install
%make_install

# Remove static libraries
rm -fv $RPM_BUILD_ROOT/%{_libdir}/libbiosig.a
rm -fv $RPM_BUILD_ROOT/%{_libdir}/libphysicalunits.a

chmod -x $RPM_BUILD_ROOT%{_mandir}/man1/{biosig_fhir,heka2itx,physicalunits,save2gdf}.1
# Remove man pages for tools that aren't included
rm -f $RPM_BUILD_ROOT/%{_mandir}/man1/{mexSLOAD,sigviewer}.1

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS README NEWS
%{_bindir}/heka2itx
%{_bindir}/physicalunits
%{_bindir}/save2aecg
%{_bindir}/save2gdf
%{_bindir}/save2scp
%{_bindir}/biosig_fhir
%{_libdir}/libbiosig.so.2
%{_mandir}/man1/*.1.gz



%files devel
%{_includedir}/%{pretty_name}-dev.h
%{_includedir}/%{pretty_name}.h
%{_includedir}/biosig2.h
%{_includedir}/gdftime.h
%{_includedir}/physicalunits.h
%{_libdir}/libbiosig2.so
%{_libdir}/libbiosig.so
%{_libdir}/pkgconfig/libbiosig.pc


%changelog
* Thu Jan 26 2023 Florian Weimer <fweimer@redhat.com> - 1.9.5-10.gita2aae2b
- Apply upstream patches to fix C99 compatibility issues

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-9.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-8.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-7.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-6.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-5.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-4.gita2aae2b
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-3.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.5-2.gita2aae2b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Aug 30 2019 Aniket Pradhan <aniket17133@iiitd.ac.in> - 1.9.5-1.gita2aae2b
- Upgraded to v1.9.5

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-3.git94296e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.3-2.git94296e0
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Nov 17 2018 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 1.9.3-1.git94296e0
- Initial build
- use make_build
