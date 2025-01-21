%{!?tcl_version: %global tcl_version %((echo '8.6'; echo 'puts $tcl_version' | tclsh 2>/dev/null) | tail -1)}
%{!?tcl_sitearch: %global tcl_sitearch %{_libdir}/tcl%{tcl_version}}

%global rev cvs20170502

Name:           tcl-togl
Version:        2.1
Release:        0.19%{?rev:.%rev}%{?dist}
Summary:        A Tk OpenGL widget

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://togl.sourceforge.net/
# cvs -z3 -d:pserver:anonymous@togl.cvs.sourceforge.net:/cvsroot/togl co -D "2017-05-02 13:00:00 UTC" Togl
# tar cjf Togl-2.1-cvs20170502.tar.bz2 Togl
Source0:        Togl-%{version}%{?rev:-%rev}.tar.bz2

Provides:       togl = %{version}-%{release}

Requires:       tcl(abi) = %{tcl_version}

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  tk-devel
BuildRequires:  libXmu-devel
BuildRequires:  mesa-libGL-devel

%description
Togl is a Tk widget for OpenGL rendering


%package devel
Summary:         Development files for %{name}
Requires:        %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for %{name}.


%prep
%autosetup -n Togl


%build
# Hackishly ensure libTogl%%{version}.so is linked against libdl (otherwise resulting library is underlinked)
LIBS="-ldl" %configure --libdir=%{tcl_sitearch} --with-tk=%{_libdir}
%make_build


%install
%make_install
rm -f %{buildroot}/%{_libdir}/Togl%{version}/LICENSE
ln -s %{tcl_sitearch}/Togl%{version}/libTogl%{version}.so %{buildroot}/%{_libdir}/libTogl%{version}.so


%files
%doc README.stubs
%license LICENSE
%{tcl_sitearch}/Togl%{version}
%{_libdir}/libTogl%{version}.so

%files devel
%{_includedir}/*
%{tcl_sitearch}/libToglstub%{version}.a


%changelog
* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.19.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Sep 04 2024 Miroslav Suchý <msuchy@redhat.com> - 2.1-0.18.cvs20170502
- convert license to SPDX

* Sat Jul 20 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.17.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sat Jan 27 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.16.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.15.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.14.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.13.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.12.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.11.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.10.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.9.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.8.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.7.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.6.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.5.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.4.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.3.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-0.2.cvs20170502
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue May 02 2017 Sandro Mani <manisandro@gmail.com> - 2.1-0.1.cvs20170502
- Update to latest snapshot (required by netgen-mesher)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jun 11 2014 Sandro Mani <manisandro@gmail.com> - 1.7-1
- Initial package
