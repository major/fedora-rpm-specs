%global	gem_name	pdfkit

Name:		rubygem-%{gem_name}
Version:	0.8.7.3
Release:	5%{?dist}

Summary:	HTML+CSS to PDF using wkhtmltopdf
# SPDX confirmed
License:	MIT
 
URL:		https://github.com/pdfkit/pdfkit
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	git
BuildRequires:	rubygems-devel

BuildRequires:	wkhtmltopdf
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(mocha)
BuildRequires:	rubygem(simplecov)
BuildRequires:	rubygem(rack)
BuildRequires:	rubygem(rack-test)
BuildRequires:	rubygem(activesupport)
BuildRequires:	%{_bindir}/xvfb-run
BuildRequires:	iputils
Requires:		wkhtmltopdf
BuildArch:		noarch

%description
Create PDFs using plain old HTML+CSS. Uses wkhtmltopdf
on the back-end which renders HTML using Webkit.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

# Clean up
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.document \
	.github \
	.gitignore \
	.rspec \
	.ruby-gemset .ruby-version \
	.travis.yml \
	Gemfile Rakefile \
	POST_INSTALL \
	*.gemspec \
	spec/ \
	%{nil}
popd

%check
disable_test() {
	filename=$1
	shift
	num=$#
	while [ $num -gt 0 ]
	do
		sed -i -e "s|it \(\"$1\"\)|xit \1|" $filename
		shift
		num=$((num - 1))
	done
}

pushd .%{gem_instdir}

disable_test spec/configuration_spec.rb \
	"detects the existance of bundler" \
	%{nil}
ping -w3 www.google.co.jp || \
	disable_test spec/pdfkit_spec.rb \
	"can handle ampersands in URLs" \
	%{nil}


xvfb-run -n 98 rspec spec/
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/LICENSE
%doc	%{gem_instdir}/CHANGELOG.md
%doc	%{gem_instdir}/README.md
%{gem_libdir}
%{gem_spec}

%exclude %{gem_cache}

%files doc
%doc	%{gem_docdir}

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7.3-1
- 0.8.7.3
- SPDX confirmed

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.7.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Thu Oct 20 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7.2-2
- 0.8.7.2

* Tue Oct 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7.1-1
- 0.8.7.1

* Mon Oct  3 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.7-1
- 0.8.7 (CVE-2022-25765, bug 2125608)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Thu Apr 14 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.6-1
- 0.8.6

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jan 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.5-1
- 0.8.5
- Fedora 34 (ruby 3.0) use webrick instead of obsolete URI::Module

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Aug 28 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.4.3.2-1
- 0.8.4.3.2

* Sun Aug  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.4.3.1-1
- 0.8.4.3.1

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sun Apr 19 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.4.2-1
- 0.8.4.2

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Mar  3 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.4.1-1
- 0.8.4.1

* Tue Feb 19 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.3-1
- 0.8.3

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 30 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.2-1
- 0.8.2

* Sun Aug 23 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.1-1
- 0.8.1

* Tue Aug 11 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.8.0-1
- 0.8.0

* Sun Aug  9 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-2
- Rewrite

* Thu May 07 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.7.0-1
- Initial package
