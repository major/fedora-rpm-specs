%if 0%{?rhel}%{?el6}%{?el7}
# see https://fedorahosted.org/fpc/ticket/395
%define _monodir %{_prefix}/lib/mono
%define _monogacdir %{_monodir}/gac
%endif

%global svn_rev 133722
%global debug_package %{nil}

Name:           gnome-keyring-sharp
Version:        1.0.1
Release:        0.44.%{svn_rev}svn%{?dist}
Summary:        Mono implementation of GNOME Keyring

License:        MIT
URL:            http://www.mono-project.com/Libraries#Gnome-KeyRing-Sharp
# Tarfile created from svn snapshot
# svn co -r %{svn-rev} \
#   svn://anonsvn.mono-project.com/source/trunk/gnome-keyring-sharp \
#   gnome-keyring-sharp-%{version}
# tar cjf gnome-keyring-sharp-%{version}-r%{svn_rev}.tar.bz2 --exclude=.svn \
#   gnome-keyring-sharp-%{version}
Source0:        gnome-keyring-sharp-%{version}-r%{svn_rev}.tar.bz2
# Patch to directly p/invoke libgnome-keyring instead of using
# deprecated socket interface taken from upstream bug report:
# https://bugzilla.novell.com/show_bug.cgi?id=589166
Patch1:         gnome-keyring-sharp-1.0.1-new-api.diff
Patch2:         gnome-keyring-sharp-1.0.1-monodoc-dir.patch

# Mono only available on these:
ExclusiveArch:  %mono_arches

BuildRequires:  autoconf automake libtool
BuildRequires:  mono-devel ndesk-dbus-devel monodoc
BuildRequires:  gtk-sharp2-devel libgnome-keyring-devel
BuildRequires: make

%description
gnome-keyring-sharp is a fully managed implementation of libgnome-keyring.

When the gnome-keyring-daemon is running, you can use this to retrive/store
confidential information such as passwords, notes or network services user
information.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files
for developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       monodoc

%description    doc
The %{name}-doc package contains documentation
for %{name}.


%prep
%setup -q
%patch -P1 -p0 -F 2 -b .new-api
%patch -P2 -p1 -b .monodoc-dir
sed -i "s#gmcs#mcs#g" configure.ac

%build
autoreconf -f -i
%configure --disable-static
make
# sharing violation when doing parallel build
#%{?_smp_mflags}


%install
%make_install
strip $RPM_BUILD_ROOT%{_libdir}/libgnome-keyring-sharp-glue.so
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%files
%doc AUTHORS ChangeLog COPYING README
%{_monodir}/gnome-keyring-sharp-1.0
%{_monogacdir}/Gnome.Keyring
%{_libdir}/libgnome-keyring-sharp-glue.so

%files devel
%{_libdir}/pkgconfig/%{name}-1.0.pc

%files doc
%{_prefix}/lib/monodoc/sources/Gnome.Keyring.*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.44.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.43.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.42.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.41.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.40.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.39.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.38.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.37.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.36.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.35.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.34.133722svn
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.33.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Feb 29 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.0.1-0.32.133722svn
- Rebuilt to fix issues with monodoc

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.31.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 06 2020 Timotheus Pokorra <timotheus.pokorra@solidcharity.com> - 1.0.1-0.30.133722svn
- Rebuilt due to mono-find-requires issue with Mono

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.29.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.28.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.27.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.26.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.25.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.24.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.23.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Oct 13 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.22.133722svn
- mono rebuild for aarch64 support

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-0.21.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.20.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue May 12 2015 Claudio Rodrigo Pereyra Diaz <elsupergomez@fedoraproject.org> 1.0.1-0.19.133722svn
- Build for Mono 4
- Use mono macros

* Tue Mar 24 2015 Than Ngo <than@redhat.com> - 1.0.1-0.18.133722svn
- use %%mono_arches

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.17.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.16.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat May 24 2014 Brent Baude <baude@us.ibm.com> - 1.0.1-0.15.133722svn
- Changed ppc64 to power64 macro

* Sat May 24 2014 Brent Baude <baude@us.ibm.com>
- rebuilt

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.13.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.12.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.11.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.10.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Oct 31 2011 Christian Krause <chkr@fedoraproject.org> - 1.0.1-0.9.133722svn
- Change paths for mono assemblies according to updated packaging
  guidelines (http://fedoraproject.org/wiki/Packaging:Mono)

* Fri Feb 25 2011 Dan Horák <dan[at]danny.cz> - 1.0.1-0.8.133722svn
- updated the supported arch list

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.7.133722svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu May 27 2010 Christian Krause <chkr@fedoraproject.org> - 1.0.1-0.6.133722svn
- Add patch to directly p/invoke libgnome-keyring instead of using
  deprecated socket interface (BZ 595457)

* Thu Aug 20 2009 Toshio Kuratomi <toshio@fedoraproject.org> - 1.0.1-0.5.133722svn%{?dist}
- Rebuild for ppc64 since previous build was obsoleted.

* Thu Aug 20 2009 Michel Salim <salimma@fedoraproject.org> - 1.0.1-0.4.133722svn%{?dist}
- Update to r133722
- Disable building on sparc64

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.3.115768svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun 01 2009 Xavier Lamien <laxathom@fedoraproject.org> - 1.0.1-0.3.115768svn
- Build arch ppc64.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-0.2.115768svn
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan 29 2009 Michel Salim <salimma@fedoraproject.org> - 1.0.1-0.1.115768svn%{?dist}
- Update to r115768

* Mon Jul 14 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.0-0.2.87622svn%{?dist}
- Disable creation of -debuginfo subpackage

* Sun Jul  6 2008 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.0-0.1.87622svn%{?dist}
- Initial package
