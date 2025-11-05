%global gem_name sequel

Name: rubygem-%{gem_name}
Version: 5.98.0
Release: 6%{?dist}
Summary: The Database Toolkit for Ruby
License: MIT
URL: http://sequel.jeremyevans.net
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: rubygem(bigdecimal)
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby >= 1.9.2
BuildArch: noarch

%description
The Database Toolkit for Ruby.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/


mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/

find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod a+x

# Run the test suite
%check
pushd .%{gem_instdir}

popd

%files
%dir %{gem_instdir}
%{_bindir}/sequel
%{gem_instdir}/bin/sequel
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}
%doc %{gem_instdir}/MIT-LICENSE

%files doc
%doc %{gem_docdir}

%changelog
* Tue Nov 04 2025 Alejandro Perez <alejandro.perez.torres@gmail.com> - 5.98.0-6
- Upgrate to 5.98.0

* Tue Aug 05 2025 Alejandro Perez <alejandro.perez.torres@gmail.com> - 5.95.1-5
 - Fix date format
* Tue Aug 05 2025 Alejandro Perez <alejandro.perez.torres@gmail.com> - 5.95.1-4
 - Fix version mistmatch
* Tue Aug 05 2025 Alejandro Perez <alejandro.perez.torres@gmail.com> - 5.95.1-3
 - Fix date on chage log
* Tue Aug 05 2025 Alejandro Perez <alejandro.perez.torres@gmail.com> - 5.95.1-2
 - Fix change log
* Tue Aug 05 2025 Alejandro Perez <alejandro.perez.torres@gmail.com> - 5.95.1-1
 - Fix conflict
  Initial package
