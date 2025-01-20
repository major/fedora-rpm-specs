%global gem_name asciidoctor-pdf

Name:     rubygem-%{gem_name}
Version:  2.3.18
Release:  3%{?dist}
Summary:  Converts AsciiDoc documents to PDF using Prawn
License:  MIT
URL:      https://github.com/asciidoctor/asciidoctor-pdf
Source0:  https://rubygems.org/gems/%{gem_name}-%{version}.gem
# git clone https://github.com/asciidoctor/asciidoctor-pdf.git && cd asciidoctor-pdf
# git checkout v2.3.18
# tar -czf rubygem-asciidoctor-pdf-2.3.18-specs-examples.tgz spec/ examples/ docs/
Source1:  %{name}-%{version}-specs-examples.tgz

BuildRequires: ruby(release)
BuildRequires: rubygems-devel >= 3.5.9
BuildRequires: ruby >= 3.3
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(asciidoctor)
BuildRequires: rubygem(prawn)
BuildRequires: rubygem(prawn-svg)
BuildRequires: rubygem(prawn-table)
BuildRequires: rubygem(prawn-templates)
BuildRequires: rubygem(prawn-icon)
BuildRequires: rubygem(treetop)
BuildRequires: rubygem(concurrent-ruby)
BuildRequires: rubygem(safe_yaml)
BuildRequires: rubygem(chunky_png)
BuildRequires: rubygem(pdf-inspector)
BuildRequires: rubygem(rouge)
BuildRequires: rubygem(coderay)
BuildRequires: rubygem(rexml)
BuildRequires: poppler-utils

BuildArch: noarch

%description
An extension for Asciidoctor that converts AsciiDoc documents to PDF using the
Prawn PDF library.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version} -b 1
mv %{_builddir}/{spec,examples} .
mv %{_builddir}/docs/modules docs/

# Regenerate the parser.
tt lib/asciidoctor/pdf/formatted_text/parser.treetop

%gemspec_remove_dep -g prawn-icon "~> 3.0.0"
%gemspec_add_dep -g prawn-icon ">= 3.0.0"
%gemspec_remove_dep -g prawn-svg "~> 0.34.0"
%gemspec_add_dep -g prawn-svg ">= 0.34.0"

%build
gem build ../%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x
rm -rf %{buildroot}%{gem_instdir}/.yardopts

%check
rspec -t '~network'

%files
%dir %{gem_instdir}
%{_bindir}/%{gem_name}
%{_bindir}/%{gem_name}-optimize
%license %{gem_instdir}/LICENSE
%doc %{gem_instdir}/README.adoc
%{gem_instdir}/bin
%{gem_instdir}/data
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NOTICE.adoc
%doc %{gem_instdir}/CHANGELOG.adoc
%doc %{gem_instdir}/docs
%{gem_instdir}/%{gem_name}.gemspec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Tue Aug 13 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.18-2
- Relax prawn-svg dependency

* Tue Jul 30 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.18-1
- Bump version to 2.3.18
- Remove relaxing rexml version, supported upstream already

* Tue Jul 23 2024 Michel Lind <salimma@fedoraproject.org> - 2.3.17-4
- Relax rexml version requirement from = to ~> 3.2.6 (rhbz#2297670)

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.17-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Wed Jun 12 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.17-2
- Relax prawn-icon dependency
- Fixes bz#2284441

* Tue Jun 04 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.17-1
- Bump to 2.3.17

* Tue May 28 2024 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.15-1
- Bump to 2.3.15

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Oct 30 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.9-1
- Bump to 2.3.9

* Fri Oct 20 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.3.8-3
- Backport upstream patch for testsuite for ruby3.3 NoMethodError
  message change

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Jun 26 2023 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.8-1
- Bump to 2.3.8

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Nov 05 2022 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.4-1
- Bump to 2.3.4
- Remove patches, already included in 2.3.4

* Wed Nov 02 2022 Sergi Jimenez <tripledes@fedoraproject.org> - 2.3.3-1
- Bump to 2.3.3

* Tue Sep 13 2022 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.2-4
- Relax praw-icon version

* Fri Sep 09 2022 Sergi Jimenez <tripledes@fedoraproject.org> - 1.6.2-3
- Add converter.rb.p0 (BZ 2113689)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Feb 22 2022 Christopher Brown <chris.brown@redhat.com> - 1.6.1-2
- Bump to 1.6.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Sep 6 2021 Christopher Brown <chris.brown@redhat.com> - 1.6.1-1
- Bump to 1.6.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Wed Jun 23 2021 Christopher Brown <chris.brown@redhat.com> - 1.5.4-4
- Re-add prawn-icon gemspec dep (BZ 1975454)

* Mon Mar 15 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.5.4-3
- Relax prawn-svg dependency for now (upstream bug 1891)

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Jan 18 2021 Christopher Brown <chris.brown@redhat.com> - 1.5.4-1
- 1.5.4
- Remove bcond now network tests are handled in code
- Update spec and example instructions

* Mon Nov 16 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-8
- Relax prawn-icon gemspec dep

* Tue Nov 3 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-7
- Relax prawn-svg gemspec dep

* Fri Aug 21 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-6
- Patch broken rouge test

* Wed Aug 19 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-5
- Relax prawn and ttfunk gemspec dependencies

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu May 7 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-3
- Further test suite patches

* Wed May 6 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-2
- Patch test suite to fix numeric asssertions

* Tue May 5 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.3-1
- Bump to 1.5.3

* Fri Feb 7 2020 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.14.beta.6
- Allow for additional failing test and warnings

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.13.beta.6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Oct 29 2019 Vít Ondruch <vondruch@redhat.com> - 1.5.0-0.12.beta.6
- Disable network depending tests.
- Relax Treetop dependency.

* Sat Oct 19 2019 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.11.beta.6
- Update to 1.5.0.beta.6
- Enable test suite

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.10.alpha.18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Jun 26 2019 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.9.alpha.18
- Update to 1.5.0.alpha.18

* Mon Apr 22 2019 Sergi Jimenez <tripledes@gmail.com> - 1.5.0-0.9.alpha.16
- Revert depending on prawn-svg 0.29.0.

* Sun Apr 14 2019 Sergi Jimenez <tripledes@gmail.com> - 1.5.0-0.8.alpha.16
- Fix BZ#1699514

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.7.alpha.16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Nov 07 2018 Christopher Brown <chris.brown@redhat.com> - 1.5.0-0.6.alpha.16
- Update to 1.5.0.alpha.16

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.6.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.5.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.4.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.3.alpha.13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 27 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.2.alpha.13
- Update to 1.5.0.alpha.13

* Sun Aug 28 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.2.alpha.12
- Update to 1.5.0.alpha.12

* Sun Aug 28 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.2.alpha.11
- Provide asciidoctor-pdf for simpler searching

* Fri Jun 17 2016 Fabio Alessandro Locati <fale@redhat.com> - 1.5.0-0.1.alpha.11
- Initial package
