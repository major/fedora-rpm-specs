%global	gem_name	image_size

Name:		rubygem-%{gem_name}
Version:	3.4.0
Release:	3%{?dist}

Summary:	Measure image size using pure Ruby
# SPDX confirmed
License:	Ruby OR GPL-2.0-only
URL:		https://github.com/toy/image_size

Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires:	ruby(release)
BuildRequires:	rubygems-devel
BuildRequires:	ruby
#%%check
BuildRequires:	rubygem(rspec)
BuildRequires:	rubygem(webrick)
BuildArch:		noarch

%description
Measure following file dimensions: apng, bmp, cur, emf, gif, heic, heif, ico, j2c, jp2,
jpeg, jpx, mng, pam, pbm, pcx, pgm, png, ppm, psd, svg, swf, tiff, webp, xbm,
xpm.


%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
Documentation for %{name}.

%prep
%autosetup -n %{gem_name}-%{version} -p1
mv ../%{gem_name}-%{version}.gemspec .

%build
gem build ./%{gem_name}-%{version}.gemspec
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.github \
	.gitignore \
	.rubocop* \
	Gemfile \
	%{gem_name}.gemspec \
	spec \
	%{nil}

popd

%check
pushd .%{gem_instdir}

# "gemspec" test reads gemspec, which needs `git',
# providing fake git.
rm -rf TMPBINDIR
mkdir TMPBINDIR
ln -sf /bin/true TMPBINDIR/git
export PATH=$(pwd)/TMPBINDIR:$PATH

rspec spec
rm -rf TMPBINDIR
popd

%files
%dir	%{gem_instdir}
%license	%{gem_instdir}/GPL
%license	%{gem_instdir}/LICENSE.txt
%doc	%{gem_instdir}/README.markdown
%{gem_libdir}
%{gem_spec}

%files doc
%doc	%{gem_docdir}
%doc	%{gem_instdir}/CHANGELOG.markdown

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.4.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Tue Jan 23 2024 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.4.0-1
- 3.4.0

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Thu Jun  1 2023 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.3.0-1
- 3.3.0

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sun Nov  6 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.2.0-1
- 3.2.0

* Sun Sep 18 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.1.0-1
- 3.1.0

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Wed Jun  1 2022 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.2-1
- 3.0.2

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Oct 22 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.1-1
- 3.0.1

* Mon Oct 18 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 3.0.0-1
- 3.0.0

* Tue Aug 24 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.2-1
- 2.1.2

* Fri Aug 20 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-3
- Fix pcx format reading on big endian system (e.g. s390x)

* Wed Aug 18 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-2
- Remove unneeded environment setting
- Disable failing test on s390x

* Thu Aug 12 2021 Mamoru TASAKA <mtasaka@fedoraproject.org> - 2.1.1-1
- Initial package
