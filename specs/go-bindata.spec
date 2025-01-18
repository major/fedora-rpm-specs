%if 0%{?fedora}
%global with_devel 1
%global with_bundled 0
%global with_debug 1
# Some tests fails and it takes a lot of time to investigate
# what is wrong
%global with_check 0
%global with_unit_test 1
%else
%global with_devel 0
%global with_bundled 1
%global with_debug 0
%global with_check 0
%global with_unit_test 0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif

%if ! 0%{?gobuild:1}
%define gobuild(o:) go build -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**}; 
%endif

%global provider        github
%global provider_tld    com
%global project         jteeuwen
%global repo            go-bindata
# https://github.com/jteeuwen/go-bindata
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     %{provider_prefix}
%global commit          a0ff2567cfb70903282db057e799fd826784d41d
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           go-bindata
Version:        3.0.7
Release:        31.git%{shortcommit}%{?dist}
Summary:        A small utility which generates Go code from any file
License:        MIT
URL:		https://%{provider_prefix}
Source0:	https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

# e.g. el6 has ppc64 arch without gcc-go, so EA tag is required
ExclusiveArch:  %{?go_arches:%{go_arches}}%{!?go_arches:%{ix86} x86_64 %{arm}}
# If go_compiler is not set to 1, there is no virtual provide. Use golang instead.
BuildRequires:  %{?go_compiler:compiler(go-compiler)}%{!?go_compiler:golang}

%description
%{summary}

This tool converts any file into managable Go source code. Useful for
embedding binary data into a go program. The file data is optionally gzip
compressed before being converted to a raw byte slice.

%prep
%setup -n go-bindata-%{commit}

%build
mkdir -p src/github.com/jteeuwen/
ln -s ../../../ src/github.com/jteeuwen/go-bindata

%if ! 0%{?with_bundled}
export GOPATH=$(pwd):%{gopath}
%else
export GOPATH=$(pwd):$(pwd)/Godeps/_workspace:%{gopath}
%endif

%gobuild -o bin/go-bindata %{import_path}/go-bindata

%install
install -d -p %{buildroot}%{_bindir}
install -m 755 bin/go-bindata %{buildroot}%{_bindir}/go-bindata

%files
%doc LICENSE README.md
%{_bindir}/go-bindata

%changelog
* Thu Jan 16 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-31.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-30.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 11 2024 Maxwell G <maxwell@gtmx.me> - 3.0.7-29.gita0ff256
- Rebuild for golang 1.22.0

* Wed Jan 24 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-28.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jan 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-27.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jul 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-26.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-25.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-24.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 3.0.7-23.gita0ff256
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Fri Jun 17 2022 Robert-André Mauchin <zebob.m@gmail.com> - 3.0.7-22.gita0ff256
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-21.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-20.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-19.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-18.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-17.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-16.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-15.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Jul 31 2018 Florian Weimer <fweimer@redhat.com> - 3.0.7-14.gita0ff256
- Rebuild with fixed binutils

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-13.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-12.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-11.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-10.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-9.gita0ff256
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Nov 01 2016 jchaloup <jchaloup@redhat.com> - 3.0.7-8.gita0ff256
- restore supported architectures
  related: #1390114

* Mon Oct 31 2016 jchaloup <jchaloup@redhat.com> - 3.0.7-7.gita0ff256
- Bump to upstream a0ff2567cfb70903282db057e799fd826784d41d
  resolves: #1390114

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-6.gitf94581b
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-5.gitf94581b
- https://fedoraproject.org/wiki/Changes/golang1.6

* Thu Feb  4 2016 Peter Robinson <pbrobinson@fedoraproject.org> 3.0.7-4.gitf94581b
- Use golang arches macro

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.7-3.gitf94581b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.7-2.gitf94581b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.6.git79847ab
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.5.git79847ab
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Oct 18 2013 Lokesh Mandvekar <lsm5@redhat.com>  0-0.4.git79847ab
- buildrequires golang

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com>  0-0.3.git79847ab
- package name change to go-bindata

* Mon Oct 14 2013 Lokesh Mandvekar <lsm5@redhat.com>  0-0.2.git79847ab
- defattr removed
- only go-bindata installed, no devel package

* Sat Oct 12 2013 Lokesh Mandvekar <lsm5@redhat.com>  0-0.1.git79847ab
- Initial fedora package
