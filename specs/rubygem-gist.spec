# Generated from gist-6.0.0.gem by gem2rpm -*- rpm-spec -*-
%global gem_name gist

Name: rubygem-%{gem_name}
Version: 6.0.0
Release: 9%{?dist}
Summary: Upload content to https://gist.github.com
License: MIT
URL: https://github.com/defunkt/gist
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: %{_bindir}/ronn
BuildRequires: rubygem(webmock)
BuildRequires: rubygem(rspec)
BuildArch: noarch

%description
Upload source code, text files and similar content to https://gist.github.com
or a local GitHub Enterprise instance.

This package provides the gist command line utility and a single function
(Gist.gist) that uploads a gist.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%setup -q -n %{gem_name}-%{version}

%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

sed  's/\xe2\x80\x8c/\* /g' README.md > README.md.ron
ronn --roff --manual="Gist manual" README.md.ron

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

mkdir -p %{buildroot}%{_mandir}/man1
%if 0%{?fedora} < 34
cp README.1 %{buildroot}%{_mandir}/man1/%{gem_name}.1
%else
cp README.md.1 %{buildroot}%{_mandir}/man1/%{gem_name}.1
%endif


%check
pushd .%{gem_instdir}
rspec spec
popd

%files
%dir %{gem_instdir}
%{_bindir}/gist
%license %{gem_instdir}/LICENSE.MIT
%{gem_instdir}/bin
%{gem_libdir}
%exclude %{gem_instdir}/vendor
%exclude %{gem_cache}
%{gem_spec}
%{_mandir}/man1/%{gem_name}.1*

%files doc
%doc %{gem_docdir}
%exclude %{gem_instdir}/.rspec
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/gist.gemspec
%{gem_instdir}/spec

%changelog
* Sat Jan 18 2025 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Fri Jul 19 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 6.0.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Sun Jul 04 2021 Georg Sauthoff <mail@gms.tf> - 6.0.0-1
- Initial package (fixes fedora#1979081)
