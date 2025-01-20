%{!?postgresql_default:%global postgresql_default 1}

%global pre Final
%global majorname postgres-decoderbufs
%global pgversion 16

Name:		postgresql%{pgversion}-decoderbufs
Version:	1.9.7
Release:	9%{?pre:.%pre}%{?dist}
Summary:	PostgreSQL Protocol Buffers logical decoder plugin

License:	MIT
URL:		https://github.com/debezium/postgres-decoderbufs

%global full_version %{version}.%{?pre:%pre}%{?!pre:Final}

Source0:	https://github.com/debezium/%{majorname}/archive/v%{full_version}.tar.gz

%if %?postgresql_default
%global pkgname %{majorname}
%package -n %{pkgname}
Summary: PostgreSQL Audit Extension
%else
%global pkgname %name
%endif

BuildRequires:	make
BuildRequires:	gcc
BuildRequires:	postgresql-server-devel >= 16, postgresql-server-devel < 17
BuildRequires:	protobuf-c-devel

Requires:	protobuf-c
Requires(pre): postgresql-server >= 16, postgresql-server < 17

%global precise_version %{?epoch:%epoch:}%version-%release
Provides: %{pkgname} = %precise_version
%if %?postgresql_default
Provides: %name = %precise_version
Provides: postgresql-%{majorname} = %precise_version
%endif
Provides: %{pkgname}%{?_isa} = %precise_version
Provides: %{majorname}-any
Conflicts: %{majorname}-any

%description
A PostgreSQL logical decoder output plugin to deliver data as Protocol Buffers messages.

%description -n %{pkgname}
A PostgreSQL logical decoder output plugin to deliver data as Protocol Buffers messages.

%if 0%{?postgresql_server_llvmjit}
%package llvmjit
Summary:	Just-in-time compilation support for %{majorname}
Requires:	%{majorname}%{?_isa} = %{version}-%{release}

%description llvmjit
Just-in-time compilation support for %{majorname}.
%endif

%prep
%autosetup -n %{majorname}-%{full_version} -p1

%build
%make_build

%install
%make_install

%files -n %{pkgname}
%doc README.md
%license LICENSE
%{_libdir}/pgsql/decoderbufs.so
%{_datadir}/pgsql/extension/decoderbufs.control

%if 0%{?postgresql_server_llvmjit}
%files llvmjit
%{_libdir}/pgsql/bitcode/decoderbufs.index.bc
%{_libdir}/pgsql/bitcode/decoderbufs/
%endif


%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-9.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Sep 16 2024 Filip Janus <fjanus@redhat.com> - 1.9.7-8.Final
- Add provide postgresqlVERSION-decoderbufs

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-7.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-6.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-5.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Dec 11 2023 Filip Janus <fjanus@redhat.com> - 1.9.7-4.Final
- Add macro postgresql_default to be able set up default version in distro
- Add symbol postgres-decoderbufs-any

* Wed Nov 29 2023 Filip Janus <fjanus@redhat.com> - 1.9.7-3.Final
- Release bump

* Tue Apr 25 2023 Filip Janus <fjanus@redhat.com> - 1.9.7-2.Final
- Version for demodularized postgresql 16

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.7-2.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Dec 02 2022 Ondřej Sloup <osloup@redhat.com> - 1.9.7-1.Final
- Rebase to the newest version
- Fix compatibility with PostgreSQL 15
- Use autosetup

* Wed Nov 16 2022 Ondřej Sloup <osloup@redhat.com> - 1.7.0-3.Final
- Rebuild for new PostgreSQL 15

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.7.0-2.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue May 10 2022 Ondrej Sloup <osloup@redhat.com> - 1.7.0-1.Final
- Fix mixed spaces and tabs
- Rebase to the latest upstream version

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-6.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Dec 15 2021 Filip Januš <fjanus@redhat.com> - 1.4.0-6.Final
- Fix requirements

* Sat Nov 06 2021 Adrian Reber <adrian@lisas.de> - 1.4.0-5.Final
- Rebuilt for protobuf 3.19.0

* Mon Oct 25 2021 Adrian Reber <adrian@lisas.de> - 1.4.0-4.Final
- Rebuilt for protobuf 3.18.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Apr 22 2021 Honza Horak <hhorak@redhat.com> - 1.4.0-2.Final
- Build jit based on what postgresql server does

* Wed Feb  3 2021 Honza Horak <hhorak@redhat.com> - 1.4.0-1.Final
- Update to new release 1.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.6.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 13 16:42:08 CET 2021 Adrian Reber <adrian@lisas.de> - 1.1.0-0.5.Final
- Rebuilt for protobuf 3.14

* Thu Sep 24 2020 Adrian Reber <adrian@lisas.de> - 1.1.0-0.4.Final
- Rebuilt for protobuf 3.13

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-0.3.Final
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Jun 14 2020 Adrian Reber <adrian@lisas.de> - 1.1.0-0.2.Final
- Rebuilt for protobuf 3.12

* Mon Mar 30 2020 Jiri Pechanec <jpechane@redhat.com> - 1.1.0-0.1.Final
- Update to 1.1.0.Final

* Mon Mar 02 2020 Sandro Mani <manisandro@gmail.com> - 1.0.0-0.1.Beta3
- Update to 1.0.0-Beta3
- Drop BR: postgis-devel

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 9 2019 - Jiri Pechanec <jpechane@redhat.com> 0.10.0-1
* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild
* Tue May 14 2019 - Jiri Pechanec <jpechane@redhat.com> 0.9.5-1
- Initial RPM packaging
