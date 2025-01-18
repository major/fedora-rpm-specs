%global srcurl    https://github.com/GNUFreetalk/%{name}

Name:             freetalk
Version:          4.1
Release:          4%{?dist}
Summary:          A console based Jabber client
License:          GPLv3+
URL:              http://www.gnu.org/software/%{name}
Source0:          %{srcurl}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:    autoconf
BuildRequires:    automake
BuildRequires:    glib2-devel
BuildRequires:    guile-devel
BuildRequires:    libcurl-devel
BuildRequires:    jansson-devel
BuildRequires:    loudmouth-devel
BuildRequires:    readline-devel
BuildRequires:    texinfo

Requires:         words
Requires(post):   info
Requires(preun):  info

%description
GNU Freetalk is a console based Jabber client. It features a readline interface
with completion of buddy names, commands, and even ordinary English words.
Freetalk is extensible, configurable, and scriptable through a Guile interface.


%prep
%setup -qn %{name}-%{version}%{?pre}

%build
./autogen.sh
%configure --disable-silent-rules --disable-rpath
%make_build

%install
%make_install

rm -rf %{buildroot}%{_infodir}/dir

# Files containing shebangs need to have the executable bits.
chmod 755 %{buildroot}%{_datadir}/%{name}/extensions/first-time-run.sh


%post
install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun
if [ $1 = 0 ]; then
  install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir >/dev/null 2>&1 || :
fi


%files
%license COPYING
%doc AUTHORS.md NEWS README* FACEBOOK.md
%doc %{_docdir}/%{name}/examples/
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_infodir}/%{name}.info*
%{_mandir}/man1/%{name}.1*


%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jan 12 2017 Igor Gnatenko <ignatenko@redhat.com> - 4.1-2
- Rebuild for readline 7.x

* Sun Nov 13 2016 Raphael Groner <projects.rg@smart.ms> - 4.1-1
- new version

* Sun Nov 13 2016 Raphael Groner <projects.rg@smart.ms> - 4.0-0.5.rc4
- modernize

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.0-0.4.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.3.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.0-0.2.rc4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Jul 02 2014 Christopher Meng <rpm@cicku.me> - 4.0-0.1.rc4
- Update to 4.0rc4

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Debarshi Ray <rishi@fedoraproject.org> - 3.2-3
- Fixed build failure with glibc-2.10.

* Tue Feb 24 2009 Release Engineering <rel-eng@fedoraproject.org> - 3.2-2
- Autorebuild for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 21 2008 Matej Cepl <mcepl@redhat.com> 3.2-1
- Version bump to 3.2.

* Wed Sep 03 2008 Debarshi Ray <rishi@fedoraproject.org> - 3.1-1
- Version bump to 3.1.
- open(2) problem fixed by upstream.

* Thu Feb 14 2008 Debarshi Ray <rishi@fedoraproject.org> - 3.0-2
- Added 'Requires: words'.

* Sat Nov 24 2007 Debarshi Ray <rishi@fedoraproject.org> - 3.0-1
- Initial build.
- Fixed sources to provide mode when using the O_CREAT flag in open(2).
