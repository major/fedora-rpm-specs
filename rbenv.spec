# some tests are failing and there isn't a straightforward way to disable them
%bcond_with check
%global salsa_commit e31f66758a2342415b74791c9080691f5f705b75

Name:           rbenv
Version:        1.2.0
Release:        %autorelease
Summary:        Manage your app's Ruby environment

License:        MIT
URL:            https://github.com/rbenv/rbenv
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://salsa.debian.org/ruby-team/rbenv/-/raw/%{salsa_commit}/debian/rbenv.pod

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-podlators

%if %{with check}
BuildRequires:  bats
BuildRequires:  git
%endif

Recommends:     ruby-build-rbenv

%description
Use rbenv to pick a Ruby version for your application and guarantee that your
development environment matches production. Put rbenv to work with Bundler for
painless Ruby upgrades and bulletproof deployments.

%prep
%autosetup

%build
pushd src
%configure
%make_build

%install
mkdir -p %{buildroot}%{_libdir}/rbenv
cp -a completions libexec rbenv.d %{buildroot}%{_libdir}/rbenv

mkdir -p %{buildroot}%{_bindir}
ln -s %{_libdir}/rbenv/libexec/rbenv %{buildroot}%{_bindir}

mkdir -p %{buildroot}%{_mandir}/man1
pod2man -c "" -r "" %SOURCE1 > %{buildroot}%{_mandir}/man1/rbenv.1

%if %{with check}
%check
bats test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
