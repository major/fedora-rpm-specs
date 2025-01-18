# https://github.com/Boomaga/boomaga/commit/7f7ad4754b20a1027c5095b660c5229353b64c8d
%global commit0 7f7ad4754b20a1027c5095b660c5229353b64c8d
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global modulename %{name}
%global __cmake_in_source_build 1

Name:           boomaga
Version:        3.3.0
Release:        22.git%{shortcommit0}%{?dist}
Summary:        A virtual printer for viewing a document before printing

# Automatically converted from old format: GPLv2 and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-only AND LicenseRef-Callaway-LGPLv2+
URL:            https://www.boomaga.org
Source0:        https://github.com/Boomaga/%{name}/archive/%{commit0}/%{name}-%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires:  cmake
BuildRequires:  cups-devel
BuildRequires:  desktop-file-utils
BuildRequires:  poppler-devel
BuildRequires:  poppler-cpp-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  snappy-devel
Requires:       cups
Requires:       shared-mime-info
Requires:       hicolor-icon-theme

%description
Boomaga (BOOklet MAnager) is a virtual printer for viewing a document
before printing it out using the physical printer.
The program is very simple to work with.
Running any program, click "print" and select "Boomaga" to see in several
seconds (CUPS takes some time to respond) the Boomaga window open.
If you print out one more document,
it gets added to the previous one, and you can also print them out as one.
Regardless of whether your printer supports duplex printing or not,
you would be able to easily print on both sides of the sheet.
If your printer does not support duplex printing,
point this out in the settings, and Booklet would ask you to turn
over the pages half way through printing your document.

The program can also help you get your documents prepared a bit
before printing. At this stage Boomaga makes it possible to:

 * Paste several documents together.
 * Print several pages on one sheet.
 * 1, 2, 4, 8 pages per sheet
 * Booklet. Folding the sheets in two, you'll get a book.

%package selinux
Summary:        SELinux policy module supporting boomaga
BuildRequires:  checkpolicy, selinux-policy-devel, hardlink
Requires:       %{name} = %{version}-%{release}
Requires(post): policycoreutils, %{name}
Requires(preun): policycoreutils, %{name}
Requires(postun): policycoreutils

%description selinux
SELinux policy module supporting boomaga

%prep
%autosetup -n %{name}-%{commit0}

# delete unused directories and files
find -name .gitignore -type f -or -name .travis.yml -type f | xargs rm -rfv

sed -i -e 's|find "/usr/local/lib" "/usr/lib" -name|find "/usr/local/lib" "%{_libdir}" -name|' scripts/testBackend.sh

%build
%cmake \
    -DUSE_QT5=Yes \
    -DCUPS_BACKEND_DIR=%{_cups_serverbin}/backend \
    -DCUPS_FILTER_DIR=%{_cups_serverbin}/filter   \
    -DSELINUX=Yes                                 \
    .
# disable parallel build, is not possible
# make_build
%cmake_build -j1

%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/%{name}/scripts
install -m 755 scripts/installPrinter.sh %{buildroot}%{_datadir}/%{name}/scripts/
chmod +x %{buildroot}%{_datadir}/%{name}/scripts/installPrinter.sh
mkdir -p %{buildroot}/%{_localstatedir}/cache/%{name}

%find_lang %{name} --with-qt

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%pre
# Start cups if is stopped
if [ "$(systemctl is-active cups.service)" != "active" ]; then
    /bin/systemctl start cups
    sleep 2
fi

%post
# Install the printer to cups backends
if [ $1 = 1 ]; then
    sh %{_datadir}/%{name}/scripts/installPrinter.sh
fi

%preun
# Uninstall the printer
if [ $1 = 0 ] ; then
    lpadmin -x "Boomaga"
fi


%post selinux
for selinuxvariant in %{selinux_variants}
do
   /usr/sbin/semodule -s ${selinuxvariant} -i \
   %{_datadir}/selinux/${selinuxvariant}/%{modulename}.pp &> /dev/null || :
   /sbin/fixfiles -R %{name} restore
done
/sbin/restorecon %{_localstatedir}/cache/%{name} || :

%preun selinux 
if [ "$1" -lt "1" ]; then # Final removal
   /usr/sbin/semodule -r %{name} 2>/dev/null || :
   /sbin/fixfiles -R %{name} restore
fi

%postun selinux
if [ $1 -eq 0 ] ; then
  for selinuxvariant in %{selinux_variants}
  do
     /usr/sbin/semodule -s ${selinuxvariant} -r %{modulename} &> /dev/null || :
  done
  [ -d %{_localstatedir}/cache/%{name} ]  && \
    /sbin/restorecon -R %{_localstatedir}/cache/%{name} &> /dev/null || :
fi


%files -f %{name}.lang
%doc README.md
%license COPYING GPL LGPL
%{_bindir}/%{name}

%{_cups_serverbin}/backend/%{name}
%dir %{_localstatedir}/cache/%{name}

%{_datadir}/applications/%{name}.desktop
%{_datadir}/dbus-1/services/org.%{name}.service

%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml

%dir %{_datadir}/ppd/%{name}
%{_datadir}/ppd/%{name}/%{name}.ppd

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/scripts
%dir %{_datadir}/%{name}/translations/
%{_datadir}/%{name}/scripts/installPrinter.sh
%{_mandir}/man1/%{name}.1.gz

%files selinux
#doc SELinux/*
%{_datadir}/selinux/*/%{modulename}.pp

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-22.git7f7ad47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Aug 28 2024 Miroslav Suchý <msuchy@redhat.com> - 3.3.0-21.git7f7ad47
- convert license to SPDX

* Thu Aug 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-20.git7f7ad47
- Rebuild for poppler 24.08.0

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-19.git7f7ad47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-18.git7f7ad47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-17.git7f7ad47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-16.git7f7ad47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-15.git7f7ad47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Aug 04 2022 Martin Gansser <martinkg@fedoraproject.org> - 3.3.0-14.git7f7ad47
- Rebuilt for rawhide
- Update to 3.3.0-14.git7f7ad47
- Add "%%global __cmake_in_source_build 1" due boomaga doesn't support out-of-src tree builds

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-13.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-12.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-11.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-10.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 04 2020 Martin Gansser <martinkg@fedoraproject.org> - 3.3.0-9.git255b54c
- Fixed FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-8.git255b54c
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-7.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-6.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Marek Kasik <mkasik@redhat.com> - 3.3.0-5.git255b54c
- Rebuild for poppler-0.84.0

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-4.git255b54c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 20 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.3.0-3.git255b54c
- Add -DSELINUX=Yes build flag for internal SELINUX support
- Update to 3.3.0-3.git255b54c

* Tue Mar 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.3.0-2.git68855ab
- Fix description
- Use HTTPS in URL
- Use %%autosetup macro

* Tue Mar 26 2019 Martin Gansser <martinkg@fedoraproject.org> - 3.3.0-1.git68855ab
- Update to 3.3.0-1.git68855ab

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-5.git7e1e19c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4.git7e1e19c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jul 05 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-3.git7e1e19c
- remove %%defattr directive from %%files section

* Tue Jun 19 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-2.git7e1e19c
- Dropped initscripts RR (BZ #1592340)

* Sun Jun 10 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.3.0-1.git7e1e19c
- Update to 1.3.0-1.git7e1e19cd

* Fri Mar 23 2018 Marek Kasik <mkasik@redhat.com> - 1.2.0-2.git4f75b03
- Rebuild for poppler-0.63.0

* Sat Mar 03 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.2.0-1.git4f75b03
- Update to 1.2.0-1.git4f75b03

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-2.git24f317b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Jan 21 2018 Martin Gansser <martinkg@fedoraproject.org> - 1.1.0-1.git24f317b
- Update to 1.1.0-1.git24f317b

* Sat Dec 02 2017 Martin Gansser <martinkg@fedoraproject.org> - 1.0.0-1.gita693dff
- Update to 1.0.0-1.gita693dff

* Wed Nov 08 2017 David Tardon <dtardon@redhat.com> - 0.9.1-7.git5ae3c05
- rebuild for poppler 0.61.0

* Fri Oct 06 2017 David Tardon <dtardon@redhat.com> - 0.9.1-6.git5ae3c05
- rebuild for poppler 0.60.1

* Fri Sep 08 2017 David Tardon <dtardon@redhat.com> - 0.9.1-5.git5ae3c05
- rebuild for poppler 0.59.0

* Sun Aug 06 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.1-4.git5ae3c05
- rebuild for poppler 0.56.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-3.git5ae3c05
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.1-2.git5ae3c05
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Jun 29 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.1-1.git5ae3c05
- Update to 0.9.1-1.git5ae3c05

* Tue Mar 28 2017 David Tardon <dtardon@redhat.com> - 0.9.0-2.git6941130
- rebuild for poppler 0.53.0

* Sun Mar 19 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.9.0-1.git6941130
- Update to 0.9.0-1.git6941130

* Wed Feb 15 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-8.gitb495615
- Update to 0.8.0-8.gitb495615

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-7.git97f52c1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 15 2017 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-6.git97f52c1
- Update to 0.8.0-6.git97f52c1
- Correct boomaga.te
- Correct boomaga.fc
- Update Scriptles
- Added RR hicolor-icon-theme

* Fri Dec 30 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-5.git074682a
- Update to 0.8.0-5.git074682a
- Change permission of %%{_cups_serverbin}/backend/%%{name} to 0700
- Add subpackage selinux (rhbz#1409115)

* Fri Dec 16 2016 David Tardon <dtardon@redhat.com> - 0.8.0-4.git157fd2e
- rebuild for poppler 0.50.0

* Thu Nov 24 2016 Orion Poplawski <orion@cora.nwra.com> - 0.8.0-3.git157fd2e
- Rebuild for poppler 0.49.0

* Fri Oct 21 2016 Marek Kasik <mkasik@redhat.com> - 0.8.0-2.git157fd2e
- Rebuild for poppler-0.48.0

* Thu Sep 22 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.8.0-1.git157fd2e
- Update to 0.8.0-1.git157fd2e

* Mon Jul 18 2016 Marek Kasik <mkasik@redhat.com> - 0.7.1-10.git9a6aa75
- Rebuild for poppler-0.45.0

* Wed May 04 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-9.git9a6aa75
- Rebuilt

* Tue May  3 2016 Marek Kasik <mkasik@redhat.com> - 0.7.1-8.git9a6aa75
- Rebuild for poppler-0.43.0

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-7.git9a6aa75
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-6.git9a6aa75
- Dropped %%Patch0
- Update to new git version

* Thu Jan 28 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-5.git2928eef
- Dropped link for %%{_bindir}/boomagamerger 
- Added %%{name}-0.7.1-NONGUI_DIR.patch

* Sat Jan 09 2016 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-4.git2928eef
- used %%{_cups_serverbin} macro provided by cups-devel
- Update to new git version

* Sat Dec 26 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-3.git8ca78b2
- Follow https://fedoraproject.org/wiki/Packaging:SourceURL
- corrected cups backend and filter directories
- use if condition in %%preun script
- linked missing %%{_bindir}/boomagamerger

* Fri Dec 25 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-2.git8ca78b2
- Rebuilt for new git release

* Tue Dec 22 2015 Martin Gansser <martinkg@fedoraproject.org> - 0.7.1-1.git8ca78b2
- Initial version of the package
