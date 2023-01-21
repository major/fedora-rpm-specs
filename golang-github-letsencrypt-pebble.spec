%bcond_without check

# https://github.com/letsencrypt/pebble
%global goipath github.com/letsencrypt/pebble
Version:        2.3.1

%gometa

%global common_description %{expand:
A miniature version of Boulder, Pebble is a small RFC 8555 ACME test server not
suited for a production certificate authority.}

%global golicenses      LICENSE
%global godocs  CODE_OF_CONDUCT.md README.md cmd/pebble-challtestsrv/challtestsrv-README.md

Name:           %{goname}
Release:        8%{?dist}
Summary:        Pebble is a miniature version of Boulder, a small RFC 8555 ACME test server

License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}

Patch1:         golang-github-letsencrypt-pebble-2.3.1-man-pages.patch

BuildRequires:  golang(github.com/letsencrypt/challtestsrv)
BuildRequires:  golang(github.com/miekg/dns)
BuildRequires:  golang(gopkg.in/square/go-jose.v2)

%description
%{common_description}

%gopkg

%prep
%goprep
%autopatch -p1
mv cmd/pebble-challtestsrv/README.md challtestsrv-README.md

%build
for cmd in cmd/p* ; do
  %gobuild -o %{gobuilddir}/bin/$(basename $cmd) %{goipath}/$cmd
done

%install
%gopkginstall
install -m 0755 -vd                     %{buildroot}%{_mandir}/man1
install -m 0755 -vd                     %{buildroot}%{_bindir}
install -m 0755 -vp %{gobuilddir}/bin/* %{buildroot}%{_bindir}/
cp -a docs/man1/pebble* %{buildroot}%{_mandir}/man1/

%if %{with check}
%check
%gocheck
%endif

%files
%license LICENSE
%doc CODE_OF_CONDUCT.md README.md challtestsrv-README.md
%{_bindir}/pebble*
%{_mandir}/man1/pebble*

%gopkgfiles

%changelog
* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jul 19 2022 Maxwell G <gotmax@e.email> - 2.3.1-6
- Rebuild for CVE-2022-{1705,32148,30631,30633,28131,30635,30632,30630,1962} in
  golang

* Sat Jun 18 2022 Robert-André Mauchin <zebob.m@gmail.com> - 2.3.1-5
- Rebuilt for CVE-2022-1996, CVE-2022-24675, CVE-2022-28327, CVE-2022-27191,
  CVE-2022-29526, CVE-2022-30629

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Dec 10 2021 Paul Wouters <paul.wouters@aiven.io> - 2.3.1-3
- Remove duplicate install command

* Thu Dec 09 2021 Paul Wouters <paul.wouters@aiven.io> - 2.3.1-2
- Add man pages from upstream commit, fix double README.MD

* Mon Nov 22 2021 Paul Wouters <paul.wouters@aiven.io> - 2.3.1-1
- Initial package
