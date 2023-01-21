Name:           gxmessage
Version:        2.20.0
Release:        24%{?dist}
Summary:        GTK2 based xmessage clone

License:        GPLv3+ and Public Domain
URL:            http://homepages.ihug.co.nz/~trmusson/programs.html#gxmessage
Source0:        http://homepages.ihug.co.nz/~trmusson/stuff/gxmessage-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(gtk+-2.0) >= 2.20.0
BuildRequires:  gettext
BuildRequires:  intltool >= 0.41.0
BuildRequires: make
Requires(post): info
Requires(preun): info


%description
Gxmassage is a GTK2 based xmessage clone. It pops up a dialog window, displays
a given message or question, then waits for the user's response. That response
is returned as the program's exit code. Because gxmessage is a drop-in 
alternative to xmessage, gxmessage accepts any option xmessage would, and 
returns the same exit codes.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}
# make sure none of the example scripts is executable
chmod 0644 examples/*


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}
# we don't need this
rm -f $RPM_BUILD_ROOT/%{_infodir}/dir

mkdir -p %{buildroot}%{_datadir}/%{name}
cat << EOF > %{buildroot}%{_datadir}/%{name}/allow_noescape
The '-noescape' option is discouraged because it can create borderless
buttonless windows that can't easily be closed. It's only available if
$prefix/share/gxmessage/allow_noescape exists.
EOF

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING COPYING.icon HACKING NEWS README TODO
%doc examples/
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}.*
%{_infodir}/%{name}.info.*
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.*


%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 11 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.20.0-13
- Remove obsolete scriptlets

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.20.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Feb 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.20.0-2
- Enable '-noescape' option

* Mon Feb 27 2012 Christoph Wickert <cwickert@fedoraproject.org> - 2.20.0-1
- Update to 2.20.0 (#797852)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Dec 06 2011 Adam Jackson <ajax@redhat.com> - 2.12.4-3
- Rebuild for new libpng

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Sep 30 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.12.4-1
- Update to 2.12.4

* Fri Sep 18 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.12.2-1
- Update to 2.12.2

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 2.12.1-1
- Update to 2.12.1
- License change to GPLv3+
- Update icon cache scriptlets

* Sat Dec 23 2006 Christoph Wickert <cwickert@fedoraproject.org> - 2.6.2-1
- Update to 2.6.2

* Sun Apr 02 2006 Christoph Wickert <fedora wickert at arcor de> - 2.6.0-1
- Update to 2.6.0
- Install examples

* Sun Nov 06 2005 Christoph Wickert <fedora wickert at arcor de> - 2.4.4-2
- Rebuild against newer gtk
- BuildRequire gettext

* Sat Jul 16 2005 Christoph Wickert <fedora wickert at arcor de> - 2.4.4-1
- Initial RPM release.
