%global	gem_name	rabbit
%define	BothRequires() \
Requires:	%1 \
BuildRequires:	%1 \
%{nil}

Name:		rubygem-%{gem_name}
Version:	3.0.3
Release:	6%{?dist}

Summary:	RD-document-based presentation application
# GPL-2.0-or-later:	overall
# The following is obtained from:
# https://www.w3.org/TR/MathML2/chapter6.html#chars.entity.tables , so from
# https://www.w3.org/TR/MathML2/overview.html , so:
# W3C:		entities/
# HPND:		lib/rabbit/trackball.rb
# From doc/en/index.rd:
# CC-BY-3.0:	data/rabbit/image/rubykaigi2011-images/rubykaigi2011-background-white.jpg
# CC-BY-3.0:	data/rabbit/image/rubykaigi2011-images/rubykaigi2011-background-black.jpg
# SPDX confirmed
License:	GPL-2.0-or-later AND W3C AND HPND AND CC-BY-3.0
URL:		http://rabbit-shocker.org/
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{name}-%{version}-test-missing-files.tar.gz
# Source1 is created by $ bash %%SOURCE2 %%version
Source2:	rabbit-create-missing-test-files.sh
Source10:	rabbit.desktop
Source11:	rabbit.xml

%BothRequires	ruby(release)
BuildRequires:	rubygems-devel
Requires:	ruby(rubygems)

%BothRequires	rubygem(coderay)
# Dependency removed on 3.0.2
#%%BothRequires	rubygem(faraday)
%BothRequires	rubygem(gettext)
%BothRequires	rubygem(gdk_pixbuf2)
%BothRequires	rubygem(gtk3)
%BothRequires	rubygem(hikidoc)
%BothRequires	rubygem(kramdown)
Requires:	rubygem-kramdown >= 2.0
%BothRequires	rubygem(kramdown-parser-gfm)
%BothRequires	rubygem(nokogiri)
%BothRequires	rubygem(poppler)
%BothRequires	rubygem(rouge)
%BothRequires	rubygem(rsvg2)
%BothRequires	rubygem(rdtool)
%BothRequires	rubygem(rttool)
%BothRequires	rubygem(rexml)
# test_codeblock_fence test needs below
# FIXME
# On F-39, python3-blockdiag is FTI because of looooong dependency chain breakage
# after python3.12 transition,
# chain beginning with python3-pycodestyle, skip this test
%if 0%{?fedora} < 39
BuildRequires:	%{_bindir}/blockdiag
%endif
BuildRequires:	desktop-file-utils
# For rabbirc
Requires:	rubygem(net-irc)
Requires:	rubygem(gdk_pixbuf2) >= 3.0.9

BuildRequires:	rubygem(racc)
BuildRequires:	rubygem(test-unit)
BuildRequires:	rubygem(test-unit-notify)
BuildRequires:	rubygem(test-unit-rr)
BuildRequires:	xorg-x11-server-Xvfb

BuildArch:	noarch
Provides:	rubygem(%{gem_name}) = %{version}

%description
Rabbit is an RD-document-based presentation application.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}

%prep
%autosetup -n %{gem_name}-%{version} -a 1 -p 1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

cp -a %{gem_name}-%{version}/test/* ./%{gem_instdir}/test/

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
	%{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Desktop, mime, icon
mkdir -p -m 0755 \
	%{buildroot}%{_datadir}/{applications/,mime/packages/}
desktop-file-install \
	--dir=%{buildroot}%{_datadir}/applications/ \
	%{SOURCE10}
install -cpm 644 %{SOURCE11} %{buildroot}%{_datadir}/mime/packages/

mkdir -p -m 0755 \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/
install -cpm 644 .%{gem_instdir}/sample/rabbit_icon.png \
	%{buildroot}%{_datadir}/icons/hicolor/32x32/apps/

# Cleanup
pushd %{buildroot}%{gem_instdir}
rm -rf \
	Gemfile \
	Rakefile \
	%{gem_name}.gemspec \
	po/ \
	test/ \
	%{nil}
popd

%find_lang rabbit
# list directories under %%{gem_instdir}/data/locale/
find %{buildroot}%{gem_instdir}/data/locale -type d | while read dir
do
	echo "%%dir ${dir#%{buildroot}}" >> rabbit.lang
done

%check
LANG=C.utf8
pushd .%{gem_instdir}

# F-39: skip blockdiag related test
%if 0%{?fedora} >= 39
sed -i.skip test/parser/test-markdown.rb \
	-e 's|\(def test_codeblock_fence\)|\1 ; omit|'
%endif

xvfb-run \
	ruby test/run-test.rb
popd

%files -f rabbit.lang
# rpmlint: keep all zero-length file
%dir	%{gem_instdir}
%doc	%{gem_instdir}/[A-Z]*

%{_bindir}/rabbit-slide
%{_bindir}/rabbit
%{_bindir}/rabbit-theme
%{_bindir}/rabbit-command
%{_bindir}/rabbirc
%{gem_instdir}/bin

%{gem_libdir}
%dir	%{gem_instdir}/data/
%{gem_instdir}/data/account.kou.gpg
%{gem_instdir}/data/rabbit/
%{gem_instdir}/entities/

%{_datadir}/applications/rabbit.desktop
%{_datadir}/mime/packages/rabbit.xml
%{_datadir}/icons/hicolor/32x32/apps/rabbit_icon.png

%exclude	%{gem_cache}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/doc/
%dir	%{gem_instdir}/misc/
%{gem_instdir}/misc/*.rb
%doc	%{gem_instdir}/misc/*/
%doc	%{gem_instdir}/sample/	

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Wed Jul  5 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-2
- Skip blockdiag integration test, python3-blockdiag now FTI
  because of loooong dependency chain breakage with python3.12

* Sun Jul  2 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.3-1
- 3.0.3

* Sat Jul  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-2
- SPDX migration

* Sat Jul  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Tue Sep 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.1-1
- 3.0.1

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Mar 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-7
- F-34: add rubygem(rexml) dep

* Mon Feb  1 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-6
- Remove old kramdown depedency stuff
- Add upstream URI.open patch to suppress warnings

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-3
- BR: rubygem(racc) for test

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-2
- Stop to use RPM rich dependency - does not seem to do as I expect

* Mon Sep  9 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-1
- 3.0.0
- Relax kramdown dependency, handle both kramdown 1.17 and 2 case

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.2.1-2
- Remove obsolete scriptlets

* Tue Sep 19 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.1-1
- 2.2.1

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Jan 23 2017 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.2.0-1
- 2.2.0

* Wed Jun  8 2016 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.9-1
- 2.1.9

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Sep 13 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.8-1
- 2.1.8

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Feb 27 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.6-1
- 2.1.6

* Tue Feb 24 2015 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.4-1
- 2.1.4

* Fri Nov  7 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.3-3
- Rescue Encoding::UndefinedConversionError on logger
  (shocker-ja:1228)

* Thu Oct 02 2014 Rex Dieter <rdieter@fedoraproject.org> 2.1.3-2
- update desktop/icon/mime scriptlets

* Wed Aug 13 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.3-1
- 2.1.3

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Mar 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.2-2
- Always call xvfb-run at %%check

* Mon Mar 17 2014 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.2-1
- 2.1.2

* Mon Dec 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-3
- Use xvfb-run on F-19

* Mon Dec 23 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-2
- Require net-irc for rabbirc
- Install desktop and mime, icon

* Sun Nov 17 2013 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-1
- Initial package
