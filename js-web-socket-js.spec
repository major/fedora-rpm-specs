%global usname web-socket-js

Name:		js-%{usname}
Version:	1.0.2
Release:	17%{?dist}
Summary:	HTML5 Web Socket implementation powered by Flash
BuildArch:	noarch
License:	BSD
URL:		https://github.com/gimite/%{usname}
Source0:	https://github.com/gimite/%{usname}/archive/v%{version}.tar.gz

BuildRequires:	web-assets-devel
BuildRequires:	uglify-js

Requires:	web-assets-filesystem


%description
%{summary}.

Note: this package ships only the java script components. The SWF
assets are not shipped as shipping binary components in Fedora without
building from source is forbidden, and currently Fedora does not have
the Apache Flex SDK packaged.

%prep
%setup -q -n %{usname}-%{version}


%build
# Presently the apache-flex-sdk is not included in Fedora, so we can't
# build the SWF assets

# Re-minify the swfobject.js file from the src directory as required
# by the packaging guidelines. It's unclear what minifier upstream
# uses for this, but we'll use uglifyjs
rm -f swfobject.js
uglifyjs src/swfobject.js -c -m -o swfobject.js

%install
mkdir -p %{buildroot}%{_jsdir}/%{usname}
cp -a swfobject.js web_socket.js %{buildroot}%{_jsdir}/%{usname}

%files
%doc LICENSE.txt NEWS.md README.md sample.html
%{_jsdir}/%{usname}


%changelog
* Thu Jul 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Oct  1 2016 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.2-5
- Fix FTBFS (BZ 1307671): use uglifyjs instead of slimit for minification

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Mar  6 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.2-3
- Own {_jsdir}/web-socket-js directory
- Introduce macro for web-socket-js string

* Fri Mar  6 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.2-2
- Minify swfobject.js from the source js file during build using slimit
- Specify noarch for package

* Thu Mar  5 2015 Jonathan Underwood <jonathan.underwood@gmail.com> - 1.0.2-1
- Initial package
