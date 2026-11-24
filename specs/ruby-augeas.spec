%global gem_name ruby-augeas

Name:           %{gem_name}
Version:        0.6.0
Release:        %autorelease
Summary:        Ruby bindings for Augeas

License:        LGPL-2.1-or-later
URL:            https://augeas.net
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/hercules-team/ruby-augeas/pull/23
# Use TypedData API needed for ruby4.1
Patch0:        ruby-augeas-pr23-TypedData-API.patch

BuildRequires:  augeas-devel >= 1.0.0
BuildRequires:  gcc
BuildRequires:  ruby-devel
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(rdoc)
BuildRequires:  rubygem(test-unit)
BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby-devel

%description
Ruby bindings for augeas.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
%autosetup -p1


%build
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a .%{gem_extdir_mri}/{gem.build_complete,*.so} %{buildroot}%{gem_extdir_mri}/

# Prevent dangling symlink in -debuginfo (rhbz#878863).
rm -rf %{buildroot}%{gem_instdir}/ext/

%check
RUBYLIB=.%{gem_extdir_mri} ruby -I.%{gem_instdir} .%{gem_instdir}/tests/*.rb


%files
%dir %{gem_instdir}
%{gem_extdir_mri}
%license %{gem_instdir}/COPYING
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/NEWS
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/tests

%changelog
%autochangelog
