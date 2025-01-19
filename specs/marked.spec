%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       marked
Version:    2.0.0
Release:    10%{?dist}
Summary:    A markdown parser for Node.js built for speed
License:    MIT
URL:        https://github.com/markedjs/%{name}
Source0:    https://github.com/markedjs/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  nodejs-packaging
BuildRequires:  web-assets-devel
BuildRequires:  uglify-js

%if 0%{?enable_tests}
BuildRequires:  jasmine
BuildRequires:  npm
#BuildRequires:  npm(express)
BuildRequires:  npm(markdown)
BuildRequires:  npm(showdown)
# Not yet packaged for Fedora.
# BuildRequires:  npm(robotskirt)
%endif

Requires:       nodejs-marked = %{version}-%{release}

%global _description\
marked is a full-featured markdown compiler that can parse huge chunks of\
markdown without having to worry about caching the compiled output or\
blocking for an unnecessarily long time.\
\
marked is extremely fast and frequently outperforms similar markdown parsers.\
marked is very concise and still implements all markdown features, as well\
as GitHub Flavored Markdown features.\
\
marked more or less passes the official markdown test suite in its entirety.\
This is important because a surprising number of markdown compilers cannot\
pass more than a few tests.

%description
Install this for command line tool and man page.
%_description

# Note: the subpackages were the only way I could get upgrades
# from marked-0.3.2 or nodejs-marked-0.3.6 to work smoothly.

%package -n nodejs-marked
Summary:    A markdown parser for JavaScript built for speed
# For symlink in %%{nodejs_sitelib}/%%{name}/lib
Requires:       js-marked = %{version}-%{release}

%description -n nodejs-marked %_description

%package -n js-marked
Summary:    Minified markdown parser for JavaScript built for speed
Requires:   web-assets-filesystem

%description -n js-marked
Install this for the minified web assests for nodejs-marked.
%_description

%prep
%setup -q -n %{name}-%{version}

# remove the bundled minified marked
rm -f marked.min.js
# Not sure what this is for, but rpmlint doesn't like it
rm -f docs/.eslintrc.json

%build
uglifyjs --comments '/Copyright/' lib/marked.js -o marked.min.js

%install
mkdir -p %{buildroot}%{_jsdir}/%{name}
cp -pr lib/marked.js marked.min.js %{buildroot}%{_jsdir}/%{name}

mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}
cp -pr package.json component.json src \
    %{buildroot}%{nodejs_sitelib}/%{name}
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}/lib
ln -sf %{_jsdir}/marked/marked.js \
    %{buildroot}%{nodejs_sitelib}/marked/lib/marked.js
mkdir -p %{buildroot}%{nodejs_sitelib}/%{name}/bin
install -p -D -m0755 bin/%{name} \
    %{buildroot}%{nodejs_sitelib}/marked/bin/%{name}
sed -i -e '1,1 s:env node:node:' \
    %{buildroot}%{nodejs_sitelib}/marked/bin/%{name}
mkdir -p %{buildroot}/%{_bindir}
ln -sf %{nodejs_sitelib}/%{name}/bin/%{name} \
    %{buildroot}%{_bindir}/%{name}

mkdir -p %{buildroot}%{_mandir}/man1
install -p -D -m0644 man/%{name}.1 \
    %{buildroot}%{_mandir}/man1/%{name}.1

%nodejs_symlink_deps


%if 0%{?enable_tests}
%check
# gfm_code_hr_list test is known to fail but the author has not yet arrived
# at a satisfactory solution: https://github.com/chjj/marked/pull/118

# def_blocks and double_link are also known to fail:
# https://github.com/chjj/marked/issues/136#issuecomment-15016714

%nodejs_symlink_deps --check
# /usr/bin/npm install robotskirt
#__nodejs ./test/
npm run test
%endif


%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%files -n nodejs-%{name}
%license LICENSE.md
%doc README.md docs
%{nodejs_sitelib}/%{name}


%files -n js-%{name}
%license LICENSE.md
%{_jsdir}/%{name}


%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jan 19 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Feb 19 2021 Stuart Gathman <stuart@gathman.org> - 2.0.0-1
- New upstream release

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Dec 15 2020 Stuart Gathman <stuart@gathman.org> - 1.2.7-1
- New upstream release

* Thu Nov 19 2020 Stuart Gathman <stuart@gathman.org> - 1.2.5-1
- New upstream release

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 22 2020 Stuart Gathman <stuart@gathman.org> - 1.1.0-3
- Move web assets to js-marked

* Fri May 22 2020 Stuart Gathman <stuart@gathman.org> - 1.1.0-2
- Move module files to nodejs-marked
- Fix shebang no longer autofixed in /usr/lib/node_modules

* Fri May 22 2020 Stuart Gathman <stuart@gathman.org> - 1.1.0-1
- New upstream release
- CVE-2015-8854 ReDos fixed in 0.3.9
- bz#1529736 bz#1529738 - XSS w/ mangling disabled fixed in 0.3.9
- bz#1702320 ReDos vuln - CVE removed, problem not in marked
- CVE-2016-1000013 fixed in 0.7.0
- CVE-2017-17461 ReDos in dependency (still open)
- CVE-2017-1000427 XSS via data URI fixed in 0.3.7

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 23 2014 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.2-2
- build browser version

* Sat Apr 19 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.3.2-1
- update to upstream release 0.3.2

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Jun 27 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.9-2
- restrict to compatible arches

* Fri May 31 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.9-1
- update to upstream release 0.2.9

* Sun Mar 17 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.8-3
- add further information about test failures (all known to fail)

* Tue Mar 12 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.8-2
- add information about test failures

* Thu Feb 14 2013 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.2.8-1
- initial package
