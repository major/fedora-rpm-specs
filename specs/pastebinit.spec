Name:           pastebinit
Version:        1.5
Release:        18%{?dist}
Summary:        Send anything you want directly to a pastebin from the command line

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://launchpad.net/pastebinit
Source0:        http://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.gz

#
# supress useless dependancy to lsb_release, folow the comportement of
# upstream by using per default fpaste.org.
# this patch musn't be push to the upstream
#
Patch0:         %{name}-1.5-delete-dependancy-to-lsb_release.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  docbook-style-xsl libxslt gettext

%description
A software that lets you send anything you want directly to a
pastebin from the command line.  This software lets you send a file
or simply the result of a command directly to the pastebin you want
(if it's supported) and gives you the URL in return.

%prep
%setup -q
%patch -P0 -p1
# Change the location of pastebin config file from /etc/pastebin.d/
# to /usr/share/pastebinit/ (unappropriate dir. name "pastebinit.d"
# + FHS)
# See https://bugs.launchpad.net/pastebinit/+bug/621923
#
sed -i "s|pastebin.d|%{name}|g" %{name} README

%build
# Generate the man page from docbook xml
xsltproc -''-nonet %{_datadir}/sgml/docbook/xsl-stylesheets*/manpages/docbook.xsl pastebinit.xml

# Build translation
pushd po
make
popd

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}%{_datadir}/
mkdir -p %{buildroot}%{_sysconfdir}/%{name}/

cp -a pastebin.d %{buildroot}%{_datadir}
mv %{buildroot}%{_datadir}/pastebin.d/ %{buildroot}%{_datadir}/%{name}/

install -m 0755 -D -p %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 -D -p %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

# Install translations
pushd po
cp -a mo %{buildroot}%{_datadir}/locale/
popd

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/%{name}/
%dir %{_sysconfdir}/%{name}/
%doc README COPYING

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 26 2024 Miroslav Suchý <msuchy@redhat.com> - 1.5-17
- convert license to SPDX

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Dec 09 2018 Miro Hrončok <mhroncok@redhat.com> - 1.5-3
- Drop unused python2-configobj dependency

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Jul 04 2018 Tony Breeds <tony@bakeyournoodle.com> - 1.5-1
- Update to 1.5 [RHBZ#1055288] [RHBZ#1472517]
- Remove defattr macro as per packaging standards

* Thu Mar 01 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.3.1-10
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 27 2012 Alexis Lameire <alexisis-pristontale@hotmail.com> - 1.3.1-1
- update to upstream release

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Lameire Alexis <alexisis-pristontale@hotmail.com> - 1.2-1
- update to 1.2 upstream release
- delete old rafb patchs
- supress dependancy to lsb_release

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Aug 24 2010 Lameire Alexis <alexisis-pristontale@hotmail.com> - 1.1-4
- add forget macro on the xslt procx

* Sun Aug 22 2010 Lameire Alexis <alexisis-pristontale@hotmail.com> - 1.1-3
- add forgotten -i option to the first sed command
- add another sed to patch the user config dir. to a proper name
- move the example conf. file yourpaste.conf to the doc. dir.
- delete BuildRoot key

* Sat Aug 21 2010 Lameire Alexis <alexisis-pristontale@hotmail.com> - 1.1-2
- make owner on the datadir
- patch source file to force config file folow the FHS

* Sun Aug 01 2010 Lameire Alexis <alexisis-pristontale@hotmail.com> - 1.1-1
- initial release
