%global debug_package %{nil}

Name:	 	mono-cecil-flowanalysis
Version:	0.1
Release:	0.47.20110512svn100264%{?dist}
Summary:	Flowanalysis engine for Cecil
URL:		https://github.com/mono/cecil/tree/master/flowanalysis
License:	MIT
# No source tarball, source from here:
# git clone https://github.com/mono/cecil.git
# mv cecil/flowanalysis flowanalysis-20110512gitb34edf6
# tar cvfj flowanalysis-20110512gitb34edf6.tar.bz2 flowanalysis-20110512gitb34edf6/
Source0:	flowanalysis-20110512gitb34edf6.tar.bz2
Source1:	cecil-flowanalysis.pc
Patch0:		flowanalysis-build.patch
BuildRequires: make
BuildRequires:	mono-devel

# Mono only available on these:
ExclusiveArch: %mono_arches

%description
Flowanalysis engine for Cecil.

%package devel
Summary:	Flowanalysis engine for Cecil
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig

%description devel
Development files for mono-cecil-flowanalysis

%prep
%setup -q -n flowanalysis-20110512gitb34edf6
%patch -P0 -p1

%build
# Use the mono system key instead of generating our own here.
cp -a /etc/pki/mono/mono.snk Cecil.FlowAnalysis.snk
make LIBDIR=%{_prefix}/lib

%install
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
cp -p %{S:1} $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
sed -i -e 's!@libdir@!${prefix}/lib!' $RPM_BUILD_ROOT/%{_libdir}/pkgconfig/cecil-flowanalysis.pc
mkdir -p $RPM_BUILD_ROOT/%{_prefix}/lib/mono/gac/
gacutil -i bin/Cecil.FlowAnalysis.dll -f -package Cecil.FlowAnalysis -root ${RPM_BUILD_ROOT}/%{_prefix}/lib


%files
%doc decompiler-notes.txt AUTHORS README
%{_prefix}/lib/mono/gac/Cecil.FlowAnalysis/
%{_prefix}/lib/mono/Cecil.FlowAnalysis/

%files devel
%{_libdir}/pkgconfig/cecil-flowanalysis.pc

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.47.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.46.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.45.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.44.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.43.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.42.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.41.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.40.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.39.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.38.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.37.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.36.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.35.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.34.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.33.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue May 29 2018 Tom Callaway <spot@fedoraproject.org> - 0.1-0.32.20110512svn100264
- fix ftbfs

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.31.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.30.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.29.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.28.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.27.20110512svn100264
- mono rebuild for aarch64 support

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.26.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 19 2016 Tom Callaway <spot@fedoraproject.org> - 0.1-0.25.20110512svn100264
- spec file cleanups

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.24.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 18 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-0.23.20110512svn100264
- Rebuild (mono4)

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.22.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.21.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.20.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.19.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.18.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.17.20110512svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Sun Nov 13 2011 Christian Krause <chkr@fedoraproject.org> - 0.1-0.16.20110512svn100264
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.14.20080409svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 11 2011 Dan Horák <dan[at]danny.cz> - 0.1-0.13.20080409svn100264
- updated the supported arch list

* Tue Oct 26 2010 Paul F. Johnson <paul@all-the-johnsons.co.uk> - 0.1-0.12.20080409svn100264
- Rebuild for mono-2.8

* Tue Dec  1 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 0.1-0.11.20080409svn100264
- use the system mono.snk key instead of regenerating on every build

* Mon Oct 26 2009 Dennis Gilmore <dennis@ausil.us> - 0.1-0.10.20080409svn100264
- ExcludeArch sparc64

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.9.20080409svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-0.8.20080409svn100264
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 30 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.1-7.5.20080409svn100264.1
- rebuild again...

* Tue Nov 25 2008 Paul F. Johnson <paul@all-the-johnsons.co.uk> 0.1-0.5.20080409svn100264.1
- rebuild against mono 2.2

* Tue Apr 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.5.20080409svn100264
- fix sed invocation

* Tue Apr 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.4.20080409svn100264
- fix libdir in pc file

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.3.20080409svn100264
- fix tag error

* Fri Apr 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.2.20080409svn100264
- specify SVN rev in comment
- add -devel package to meet Mono guidelines

* Wed Apr 9 2008 Tom "spot" Callaway <tcallawa@redhat.com> 0.1-0.1.20080409svn100264
- Initial package creation
