Name:           license-validate
Version:        25
Release:        3%{?dist}
Summary:        Validate SPEC license string

License:        MIT
URL:            https://pagure.io/copr/license-validate/
# source is created by:
# git clone https://pagure.io/copr/license-validate.git
# cd license-validate; tito build --tgz
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       fedora-license-data >= 1.18
BuildRequires:  fedora-license-data >= 1.18
BuildRequires:  python3-devel

# man pages
BuildRequires:  asciidoc
BuildRequires:  libxslt

# for test
BuildRequires:  (python3dist(lark) or python3dist(lark-parser))
Requires:       (python3dist(lark) or python3dist(lark-parser))


%description
Validate whether the license string conforms to Fedora Licensing.


%prep
%autosetup


%build
./generate-shortnames.py > fedora-shortnames.txt
./create-grammar.py grammar-shortnames.lark fedora-shortnames.txt > full-grammar-shortnames.lark
for i in license-validate.1.asciidoc license-fedora2spdx.asciidoc; do
  a2x -d manpage -f manpage "$i"
done


%install
mkdir -p %{buildroot}%{_bindir}
install license-validate.py %{buildroot}%{_bindir}/license-validate
install license-fedora2spdx.py %{buildroot}%{_bindir}/license-fedora2spdx

mkdir -p %{buildroot}%{_datadir}/%{name}/
install -m644 full-grammar-shortnames.lark %{buildroot}%{_datadir}/%{name}/grammar-shortnames.lark

mkdir -p %{buildroot}%{_mandir}/man1
install -m644 license-validate.1 %{buildroot}/%{_mandir}/man1/
install -m644 license-fedora2spdx.1 %{buildroot}/%{_mandir}/man1/

%check
./validate-grammar.py full-grammar-shortnames.lark

%files
%license LICENSE
%doc README.md
%{_bindir}/license-validate
%{_bindir}/license-fedora2spdx
%{_datadir}/%{name}
%doc %{_mandir}/man1/license-validate.1*
%doc %{_mandir}/man1/license-fedora2spdx.1*


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Jun 30 2024 Miroslav Suchý <msuchy@redhat.com> 25-1
- allow lowercase variants as part of spdx 3.0

* Sun Jun 30 2024 Miroslav Suchý <msuchy@redhat.com> 24-1
- allow lowercase variants as part of spdx 3.0

* Thu Apr 11 2024 Miroslav Suchý <msuchy@redhat.com> 23-1
- lark-parser was renamed to lark, allow both

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Oct 26 2023 Miroslav Suchý <msuchy@redhat.com> 22-1
- allow to pass --package and do not print error when package is known to use
  not-allowed license as an exception
- better wording

* Thu Oct 19 2023 Miroslav Suchý <msuchy@redhat.com> 21-1
- when license is not allowed print known packages that can use it as an
  exception
- Print 'usage' if the license is not allowed.

* Fri Aug 04 2023 Miroslav Suchý <msuchy@redhat.com> 20-1
- print note if string passed to license-fedora2spdx is already SPDX formula

* Thu Apr 20 2023 Miroslav Suchý <msuchy@redhat.com> 19-1
- use spdx grammar from fedora-license-data

* Thu Apr 06 2023 Miroslav Suchý <msuchy@redhat.com> 18-1
- SPDX identifier are case insensitive

* Fri Dec 30 2022 Miroslav Suchý <msuchy@redhat.com> 17-1
- add python as BR

* Fri Dec 30 2022 Miroslav Suchý <msuchy@redhat.com> 16-1
- use correct legacy shortnames

* Fri Dec 30 2022 Miroslav Suchý <msuchy@redhat.com> 15-1
- use new format of fedora-licenses.json

* Wed Nov 16 2022 Miroslav Suchý <msuchy@redhat.com> 14-1
- stress the need to choose licesense when there is more options

* Thu Nov 10 2022 Miroslav Suchý <msuchy@redhat.com> 13-1
- add variation only if it not there yet

* Mon Oct 24 2022 Miroslav Suchý <msuchy@redhat.com> 12-1
- 2137269 - fedora2spdx: ignore licenses which does not have fedora abbrev

* Tue Oct 04 2022 Miroslav Suchý <msuchy@redhat.com> 11-1
- rebuild with new data

* Sat Sep 10 2022 Miroslav Suchý <msuchy@redhat.com> 10-1
- fix text of the license
- be more friendly when user pass invalid license

* Mon Jul 18 2022 Miroslav Suchý <msuchy@redhat.com> 9-1
- 2108165 - upper case AND/OR in resulting SPDX formula (msuchy@redhat.com)

* Sat Jun 04 2022 Miroslav Suchý <msuchy@redhat.com> 8-1
- do not require param for --old

* Sat Jun 04 2022 Miroslav Suchý <msuchy@redhat.com> 7-1
- BR fedora-license-data (msuchy@redhat.com)

* Sat Jun 04 2022 Miroslav Suchý <msuchy@redhat.com> 6-1
- add rawhide releaser
- validate using SPDX and introduce --old for previous behaviour
- migrate to fedora-license-data
- add helpers to generate list of licenses from fedora-license-data

* Fri Apr 22 2022 Miroslav Suchý <msuchy@redhat.com> 5-1
- 2077908 - add missing requires on rpminspect-data-fedora (msuchy@redhat.com)
- fix man page (msuchy@redhat.com)

* Wed Apr 06 2022 Miroslav Suchý <msuchy@redhat.com> 4-1
- add license-fedora2spdx to package
- add script to convert from Fedoras shortname to SPDX identifier

* Wed Jan 05 2022 Miroslav Suchý <msuchy@redhat.com> 3-1
- fixes for package review
- code cleanup
- catch all lark errors
- allow bad license with or operator
- add comment aboutlicense_item
- add general redistributable license
- add missing OFL license
- add scripts to check all fedora licenses
- add man page
- remove COMMENTS from grammar

* Sun Dec 26 2021 Miroslav Suchý <msuchy@redhat.com> 2-1
- correctly handle parenthesis (msuchy@redhat.com)
- grammar fixes (msuchy@redhat.com)

* Sun Dec 26 2021 Miroslav Suchý <msuchy@redhat.com> 1-1
- initial package
