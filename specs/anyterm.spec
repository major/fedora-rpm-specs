Name: anyterm
Version: 1.2.3
Release: 22%{?dist}
Summary: A web-based terminal emulator

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://anyterm.org

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export http://svn.anyterm.org/anyterm/tags/releases/1.2/1.2.3 anyterm-1.2.3
#  tar -jcf anyterm-1.2.3.tar.xz anyterm-1.2.3
Source0: anyterm-1.2.3.tar.xz
Source1: anyterm-cmd
Source4: anyterm.conf
Source5: anyterm.service

# http://anyterm.org/1.1/install.html#secid2252601
Patch0: anyterm-change-url-prefix.patch

BuildRequires:  gcc-c++
BuildRequires: boost-devel  
BuildRequires: zlib-devel
BuildRequires: systemd
BuildRequires: make
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd


%package httpd
Summary: Httpd proxy configuration for anyterm
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
Requires: %{name} = %{version}-%{release}
Requires: httpd


%description
The Anyterm web-based terminal emulator, permits terminal and/or arbitrary
command access via http. The anyterm daemon can be configured to run any
arbitrary command, redirecting all standard input / output / error to 
and from any javascript-enabled web browser in real time.

%description httpd
The httpd configuration necessary to proxy anyterm.

%prep
%setup -q
%patch -P0 -p0

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++17"
make %{?_smp_mflags} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" OPTIMISE_FLAGS="$CXXFLAGS"
gzip anytermd.1

%install
install -Dp -m0755 anytermd %{buildroot}%{_sbindir}/anytermd
install -Dp -m0644 anytermd.1.gz %{buildroot}%{_mandir}/man1/anytermd.1.gz
install -Dp -m0755 %{SOURCE1} %{buildroot}%{_libexecdir}/%{name}/anyterm-cmd
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/httpd/conf.d/anyterm.conf
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_unitdir}/anyterm.service

mkdir -p %{buildroot}%{_datadir}/anyterm/
for f in browser/*.{html,css,js,png,gif}; do
   install -m644 "$f" %{buildroot}%{_datadir}/anyterm/
done

# Create a home directory for the user.
mkdir -p -m755 %{buildroot}%{_localstatedir}/run/%{name}
mkdir -p %{buildroot}%{_sysconfdir}/tmpfiles.d
cat <<EOF > %{buildroot}%{_sysconfdir}/tmpfiles.d/%{name}.conf
d %{_localstatedir}/run/%{name} 0755 root %{name}
EOF


%pre
# create anyterm group / user
getent group %{name} >/dev/null 2>&1 || \
   groupadd -r %{name}
getent passwd %{name} >/dev/null 2>&1 || \
  useradd -r -l -g %{name} -s /sbin/nologin \
  -d %{_localstatedir}/run/%{name} -c "Anyterm service" %{name}
if [[ ! -d %{_localstatedir}/run/%{name} ]]; then
  mkdir -m755 %{_localstatedir}/run/%{name}
  chown %{name}:%{name} %{_localstatedir}/run/%{name}
fi
if [[ $(getent passwd %{name} | cut -d: -f6) == /dev/null ]]; then
  usermod -d %{_localstatedir}/run/%{name} %{name}
fi
exit 0

%post
%systemd_post anyterm.service

%preun
%systemd_preun anyterm.service

%postun
%systemd_postun_with_restart anyterm.service 

%files
%{_sbindir}/anytermd
%{_libexecdir}/anyterm/
%{_mandir}/man1/anytermd.1.gz
%{_datadir}/anyterm/
%{_unitdir}/anyterm.service
%ghost %attr(0755,%{name},%{name}) %dir %{_localstatedir}/run/%{name}
%{_sysconfdir}/tmpfiles.d/%{name}.conf
%doc LICENSE

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/anyterm.conf

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul  25 2024 Miroslav Suchý <msuchy@redhat.com> - 1.2.3-21
- convert license to SPDX

* Wed Jul 17 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 17 2024 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-17
- Rebuilt for Boost 1.83

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Feb 20 2023 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-15
- Rebuilt for Boost 1.81

* Wed Jan 18 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jul 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed May 04 2022 Thomas Rodgers <trodgers@redhat.com> - 1.2.3-12
- Rebuilt for Boost 1.78

* Wed Jan 19 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Aug 06 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-10
- Rebuilt for Boost 1.76

* Wed Jul 21 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 02 2021 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.2.3-8
- Rebuilt for updated systemd-rpm-macros
  See https://pagure.io/fesco/issue/2583.

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Jan 22 2021 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-6
- Rebuilt for Boost 1.75

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 28 2020 Jonathan Wakely <jwakely@redhat.com> - 1.2.3-3
- Rebuilt for Boost 1.73

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 17 2019 Alexander Boström <abo@root.snowtree.se> - 1.2.3-1
- upgrade to 1.2.3

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-47
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-46
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Jonathan Wakely <jwakely@redhat.com> - 1.1.29-45
- Rebuilt for Boost 1.69

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-44
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-43
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Jan 23 2018 Jonathan Wakely <jwakely@redhat.com> - 1.1.29-42
- Rebuilt for Boost 1.66

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-41
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-40
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Jul 19 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.29-39
- Rebuilt for s390x binutils bug

* Mon Jul 03 2017 Jonathan Wakely <jwakely@redhat.com> - 1.1.29-38
- Rebuilt for Boost 1.64

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-37
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Feb 23 2016 Yaakov Selkowitz <yselkowi@redhat.com> - 1.1.29-36
- Specify C++98 usage (#1307317)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.29-35
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Jonathan Wakely <jwakely@redhat.com> - 1.1.29-34
- Rebuilt for Boost 1.60

* Fri Aug 28 2015 Jonathan Wakely <jwakely@redhat.com> 1.1.29-33
- Patched and rebuilt for Boost 1.59

* Wed Aug 05 2015 Jonathan Wakely <jwakely@redhat.com> 1.1.29-32
- Rebuilt for Boost 1.58

* Sat Aug 01 2015 Alexander Boström <abo@root.snowtree.se> - 1.1.29-31
- fix build without prelink

* Sat Aug 01 2015 Alexander Boström <abo@root.snowtree.se> - 1.1.29-30
- remove prelink buildreq

* Wed Jul 29 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-29
- Rebuilt for https://fedoraproject.org/wiki/Changes/F23Boost159

* Wed Jul 22 2015 David Tardon <dtardon@redhat.com> - 1.1.29-28
- rebuild for Boost 1.58

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-27
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 1.1.29-26
- Rebuilt for GCC 5 C++11 ABI change

* Tue Jan 27 2015 Petr Machata <pmachata@redhat.com> - 1.1.29-25
- Rebuild for boost 1.57.0

* Fri Aug 15 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Peter Robinson <pbrobinson@fedoraproject.org> 1.1.29-23
- No prelink on aarch64 ppc64le
- Cleanup spec and update systemd scriptlets

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 Petr Machata <pmachata@redhat.com> - 1.1.29-21
- Rebuild for boost 1.55.0

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul 30 2013 Petr Machata <pmachata@redhat.com> - 1.1.29-19
- Rebuild for boost 1.54.0

* Sat Feb 23 2013 Alexander Boström <abo@root.snowtree.se> - 1.1.29-18
- Add patch to build with boost 1.53 (rhbz #913877)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jun  2 2012 Alexander Boström <abo@root.snowtree.se> - 1.1.29-15
- Really create the home directory.

* Fri Jun  1 2012 Alexander Boström <abo@root.snowtree.se> - 1.1.29-14
- Actually create the home directory on first install.

* Fri Jun  1 2012 Alexander Boström <abo@root.snowtree.se> - 1.1.29-13
- Fix spec file typo.
- Create a home directory for the Anyterm user.

* Tue May 22 2012 Alexander Boström <abo@root.snowtree.se> - 1.1.29-12
- Remove SysV script, add systemd service file.
- Fix anyterm-cmd.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-11
- Rebuilt for c++ ABI breakage

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.29-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul  15 2009  <mmorsi@redhat.com> - 1.1.29-8
- correct anyterm dependency for anyterm-httpd subpkg
- removed useradd/group add stdout redirection
- def attr for anyterm-httpd subpkg
- slight rewording and other trivial tasks

* Tue Jul  14 2009  <mmorsi@redhat.com> - 1.1.29-7
- removed useradd/group add stderr redirection
- used all macros where i could
- create httpd subpackage for anyterm/httpd integration

* Mon Jul  13 2009  <mmorsi@redhat.com> - 1.1.29-6
- fixed location of %%doc macro, and resolved other
  macro issues
- moved anyterm-cmd from bindir to libexecdir/anyterm

* Thu Jul  09 2009  <mmorsi@redhat.com> - 1.1.29-5
- added CFLAGS / CXXFLAGS to pick up RPM_OPT_FLAGS

* Tue Jul  07 2009  <mmorsi@redhat.com> - 1.1.29-4
- removed pbuild
- removed executable stack (requires prelink/execstack)

* Thu Apr  09 2009  <mmorsi@redhat.com> - 1.1.29-3
- updated spec / init based on rpmlint output

* Wed Apr  08 2009  <mmorsi@redhat.com> - 1.1.29-2
- Serve static content via apache
- Use 1.1.29 release and newly added patches

* Mon Mar  16 2009  <mmorsi@redhat.com> - 1.1.29-1
- Initial checkout and build.
