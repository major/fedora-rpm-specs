Name:           wiki2beamer
Version:        0.10.0
Release:        10%{?dist}
Summary:        Converts a simple wiki-like syntax to complex LaTeX beamer code
# Code is GPLv2+, documentation is GFDL
License:        GPLv2+ and GFDL
BuildArch:      noarch
BuildRequires:  python3-devel
# For generating man page
BuildRequires:  rubygem-asciidoctor
URL:            https://github.com/wiki2beamer/wiki2beamer
Source0:        https://github.com/wiki2beamer/wiki2beamer/archive/%{name}-v%{version}/%{name}-%{version}.tar.gz

%description
Wiki2beamer converts a simple wiki-like syntax to complex LaTeX beamer code. 
It's written in python and should run on windows and all *nix platforms. Why 
collaborative? Because you can use it with version control systems. Afraid 
to loose some LaTeX powers? Don't worry: you can always fall back to plain 
LaTeX as wiki2beamer is just a preprocessor.

%prep
%setup -q -n %{name}-%{name}-v%{version}

for file in code/wiki2beamer tests/test_wiki2beamer.py; do
    sed -i '1s|^#!/usr/bin/env python|#!%{__python3}|' $file
done
mv doc/fdl.txt doc/LICENSE-DOCS

%build
pushd code/
%{__python3} setup.py build
popd

%install
pushd code/
%{__python3} setup.py install --skip-build --root %{buildroot}
popd

pushd doc/man/
asciidoctor -b manpage %{name}.adoc
install -p -m644 -D %{name}.1 %{buildroot}/%{_mandir}/man1/%{name}.1
popd

rm -r %{buildroot}/%{python3_sitelib}

%check
pushd tests
./test_wiki2beamer.py
popd

%files
%doc ChangeLog LICENSE README.md doc/LICENSE-DOCS doc/examples
%{_bindir}/wiki2beamer
%{_mandir}/man1/wiki2beamer.1*

%changelog
* Sat Jul 22 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sat Jan 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Sat Jan 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Mar 01 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 0.10.0-1
- Update to 0.10.0, fixing Python 3.3 incompability.
- Upstream moved to GitHub, also enable tests.

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-15
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.9.5-11
- Rebuild for Python 3.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Nov 14 2015 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.9.5-9
- Switch to python3

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Oct 04 2012 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.9.5-4
- Email address in changelog
- Remove the clean tag
- Add README to doc

* Thu Oct 04 2012 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.9.5-3
- Macro consistency

* Sat Sep 22 2012 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.9.5-2
- Fix release tag
- Not cleaning the buildroot(obsolete)
- Renamed fdl.txt to LICENSE-DOCS

* Mon Aug 27 2012 Sebastian Dyroff <sdyroff@fedoraproject.org> - 0.9.5-1
- Initial package
