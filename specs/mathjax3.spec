Name:		mathjax3
Version:	3.2.2
Release:	7%{?dist}
Summary:	JavaScript library to render math in the browser
License:	Apache-2.0 AND 0BSD AND BSD-2-Clause AND BSD-2-Clause-Views AND BSD-3-Clause AND CC-BY-4.0 AND ISC AND (LGPL-2.0-only OR MIT) AND MIT
URL:		https://mathjax.org
Source0:	https://github.com/mathjax/MathJax-src/archive/%{version}/MathJax-src-%{version}.tar.gz
#		Additional node modules needed to build from source
Source1:	MathJax-src-%{version}-node-modules.tar.gz
#		Script to create the above sources
Source2:	create-source.sh
BuildArch:	noarch
BuildRequires:	npm
BuildRequires:	web-assets-devel
Requires:	web-assets-filesystem

%description
MathJax is an open-source JavaScript display engine for LaTeX, MathML,
and AsciiMath notation that works in all modern browsers. It requires no
setup on the part of the user (no plugins to download or software to
install), so the page author can write web documents that include
mathematics and be confident that users will be able to view it
naturally and easily. Supports LaTeX, MathML, and AsciiMath notation
in HTML pages.

%prep
%setup -q -a 1 -n MathJax-src-%{version}

# Disable minimizing of javascript components
sed 's!minimize: true!minimize: false!' -i components/webpack.common.js

# https://bugzilla.redhat.com/show_bug.cgi?id=2244891
# https://github.com/alexei/sprintf.js/issues/211
# https://github.com/alexei/sprintf.js/pull/212
sed 's!BSD-3-Clause-Clear!BSD-3-Clause!' -i node_modules/sprintf-js/bower.json

%build
npm run compile
npm run make-components

%install
mkdir -p %{buildroot}%{_jsdir}/mathjax@3
cp -pr es5 %{buildroot}%{_jsdir}/mathjax@3

%files
%{_jsdir}/mathjax@3
%doc README.md
%license LICENSE

%changelog
* Fri Jan 17 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Thu Jul 18 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Thu Jan 25 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Sun Jan 21 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Oct 20 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.2-3
- Correct license tag (rhbz#2244891)

* Thu Jul 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Mar 09 2023 Mattias Ellert <mattias.ellert@physics.uu.se> - 3.2.2-1
- Initial mathjax version 3 package for Fedora and EPEL
