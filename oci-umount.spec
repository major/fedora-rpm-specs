%global provider        github
%global provider_tld    com
%global project         projectatomic
%global repo            oci-umount
# https://github.com/projectatomic/oci-umount
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          c3cda1f73034ca5647bfe4417039a7bbf52b5361
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           oci-umount
Epoch:          2
Version:        2.5
Release:        9.git%{shortcommit}%{?dist}
Summary:        OCI umount hook for docker
License:        GPLv3+
URL:            https://%{provider_prefix}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz
#exclude ppc64, the same arches as docker
ExclusiveArch: %{ix86} x86_64 %{arm} aarch64 ppc64le s390x %{mips}


Obsoletes: docker-oci-umount < 2:1.13.1-13

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(yajl)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(mount)
BuildRequires:  go-md2man
BuildRequires:  pcre-devel

%description
OCI umount hooks umount potential leaked mount points in a containers
mount name-spaces

%prep
%setup -q -n %{name}-%{commit}

%build
autoreconf -i
%configure --libexecdir=%{_libexecdir}/oci/hooks.d/
%make_build

%install
%make_install
install -d %{buildroot}%{_datadir}/%{name}/%{name}.d

%files
%{_libexecdir}/oci/hooks.d/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man5/%{name}-options.conf.5*
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/%{name}.conf
%dir %{_libexecdir}/oci
%dir %{_libexecdir}/oci/hooks.d
%dir %{_datadir}/containers/oci/hooks.d
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{name}.d
%{_datadir}/%{name}/oci-umount-options.conf
%{_datadir}/containers/oci/hooks.d/%{name}.json
%ghost %{_sysconfdir}/%{name}/%{name}.d
%ghost /etc/oci-umount/oci-umount-options.conf

%changelog
* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-9.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-8.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-7.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-6.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-5.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-4.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Oct 06 2019 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.5-3.gitc3cda1f
- Resolves: #1736363 - update dep

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.5-2.gitc3cda1f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 1 2019 Dan Walsh <dwalsh@redhat.com> - 2:2.5-1.git
- Add Man page
- Fix converity issues.

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.3.4-2.git87f9237
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 28 2018 Dan Walsh <dwalsh@redhat.com> - 2:2.3.4-1.git
- Add new paths for CRI-O

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2:2.3.3-2.gite3c9055
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Dan Walsh <dwalsh@redhat.com> - 2:2.3.3-1.git
- Support passing of stage via stage environment variable.

* Thu Dec 21 2017 Dan Walsh <dwalsh@redhat.com> - 2:2.3.2-1.git
- Fix oci-umount.json to run in stages to support CRI-O

* Tue Nov 7 2017 Dan Walsh <dwalsh@redhat.com> - 2:2.3.1-1.git51e7c505
-  Provide a knob log_level to control verbosity of messages

* Thu Sep 21 2017 Dan Walsh <dwalsh@redhat.com> - 2:2.2.0-2.git0a4dcd6
* Thu Sep 21 2017 Dan Walsh <dwalsh@redhat.com> - 2:2.2.0-2.git0a4dcd6
- Add support for multiple configuration files.
  oci-umount will still read config file /etc/oci-umount.conf if it
  exists, but will also read config files in /usr/share/oci-umount/oci-umount.d
  and config files in /etc/oci-umount/oci-umount.d.  If the same file name exists
  in both directories, then oci-umount will only use the content in /ect/oci-umount/oci-umount.d.
- Make Logs less noisy
- Improve logs output, adding containier id, and needed file information
- Add support for specifying submounts PATH/* will unmount all mountpoints 
  under PATH in a container
- Support for oci configuration files to specify when to run the plugin

* Thu Sep 21 2017 Lokesh Mandvekar <lsm5@fedoraproject.org> - 2:2.2.0-1.git0a4dcd6
- bump to v2.2.0

* Thu Aug 17 2017 Frantisek Kluknavsky <fkluknav@redhat.com> - 2:2.0.0-2.gitf90b64c
- rebased to f90b64c144ff1a126f7c57b32396e8990ca696fd

* Thu Jul 27 2017 Frantisek Kluknavsky <fkluknav@redhat.com> - 2:1.13-103.git7623f6a
- obsolete with epoch

* Thu Jul 20 2017 fkluknav <fkluknav@redhat.com> - 2:1.13-102.git7623f6a
- fixes according to package review

* Mon Jul 17 2017 fkluknav <fkluknav@redhat.com> - 2:1.13-101.git7623f6a
- adapted for Fedora, versioning continues from the current docker version

* Wed May 17 2017 Dan Walsh <dwalsh@redhat.com> - 0.1.1
- Initial RPM release
