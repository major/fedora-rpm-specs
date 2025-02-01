%global	gem_name	tk

Name:		rubygem-%{gem_name}
Version:	0.5.1
Release:	4%{?dist}

Summary:	Tk interface module using tcltklib
# SPDX confirmred
#
# Some license texts under sample/ such as
## sample/demos-jp/doc.org/license.terms
# or so are all TCL
#
# MIT-CMU: sample/tkextlib/iwidgets/catalog_demo/Orig_LICENSE.txt
# MIT-CMU: sample/tkextlib/tile/Orig_LICENSE.txt
License:	BSD-2-Clause OR Ruby
URL:		https://github.com/ruby/tk
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/ruby/tk/pull/66
# Support C23 with strict function prototype declaration
Patch0:	rubygem-tk-pr66-c23-fuction-prototype.patch

BuildRequires:	gcc
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby-devel
BuildRequires:	pkgconfig(tk) <= 8.999
Obsoletes:		ruby-tcltk < 2.4.0
# No provides for now

%description
Tk interface module using tcltklib.

%package	doc
Summary:	Documentation for %{name}
License:	(BSD-2-Clause OR Ruby) AND TCL AND MIT-CMU
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1 -b .c23
mv ../%{gem_name}-%{version}.gemspec .

%build
grep -rlZ /usr/local/bin . | \
	xargs -0 sed -i -e 's|/usr/local/bin|%{_bindir}|g'
grep -rlZ /usr/bin/env . | \
	xargs -0 sed -i -e 's|/usr/bin/env ruby|%{_bindir}/ruby|'
find . -name \*.rb -print0 | xargs -0 grep -lZ '^#![ \t]*%{_bindir}' | \
	xargs -0 sed -i -e '\@^#![ \t]*%{_bindir}@d'
find . -name \*.rb -print0 | xargs -0 chmod 0644
find sample -type f -print0 | xargs -0 grep -lZ '^#![ \t]*%{_bindir}' | \
	xargs -0 chmod 0755

gem build %{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/* \
	%{buildroot}%{gem_extdir_mri}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.github \
	.gitignore \
	.travis.yml \
	Gemfile \
	README.macosx-aqua \
	README.tcltklib \
	Rakefile \
	old-README.tcltklib.ja \
	%{gem_name}.gemspec \
	bin/ \
	ext/ \
	%{nil}
popd
pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	mkmf.log \
	gem_make.out \
	%{nil}
popd

%check
# No check currently

%files
%dir %{gem_instdir}
%license	%{gem_instdir}/BSDL
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.1st
%doc	%{gem_instdir}/README.md

%{gem_libdir}/

%{gem_extdir_mri}/
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/README.fork
# Some files under the following are under TCL
%{gem_instdir}/sample/

%doc	%{gem_instdir}/README.ActiveTcl
%doc	%{gem_instdir}/MANUAL_tcltklib.eng
%doc	%lang(ja) %{gem_instdir}/MANUAL_tcltklib.ja

%changelog
* Fri Jan 31 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-4
- Use tk8 explicitly

* Sun Jan 19 2025 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Wed Jan 15 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-2
- Apply upstream PR to support C23 strict function prototype

* Tue Jan 14 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.1-1
- 0.5.1

* Tue Jan 07 2025 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-5
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.4

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Wed Jan 03 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-2
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.3

* Sun Nov 12 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.5.0-1
- 0.5.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Wed Jan 04 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-7
- Rebuild for https://fedoraproject.org/wiki/Changes/Ruby_3.2

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jan 26 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-5
- F-36: rebuild against ruby31

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Tue Mar 30 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-2
- Add %%lang for some file

* Sun Mar 28 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.4.0-1
- 0.4.0

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Jan 06 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-2
- F-34: rebuild against ruby 3.0

* Fri Oct  9 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.3.0-1
- 0.3.0

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jan 17 2020 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-9
- F-32: rebuild against ruby27

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jan 21 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-6
- F-30: rebuild against ruby26

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 20 2018 Björn Esser <besser82@fedoraproject.org> - 0.2.0-3
- Rebuilt for switch to libxcrypt

* Wed Jan 03 2018 Mamoru TASAKA <mtasaka@fedoraproject.org> - 0.2.0-2
- F-28: rebuild for ruby25

* Fri Aug  4 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.2.0-1
- 0.2.0

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 27 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.1.2-2
- Reflect comments on review request

* Wed Mar 15 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.1.2-1
- 0.1.2

* Sun Jan  1 2017 Mamoru TASAKA <mtasaka@tbz.t-com.ne.jp> - 0.1.1-1
- Initial package
