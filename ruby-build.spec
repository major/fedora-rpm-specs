# some tests are failing and there isn't a straightforward way to disable them
%bcond_with check
%global salsa_commit 4855a775cf29a175afe605ee7ea43134e29a4b40

%global debug_package %{nil}

Name:           ruby-build
Version:        20221004
Release:        %autorelease
Summary:        Compile and install Ruby

License:        MIT
URL:            https://github.com/rbenv/ruby-build
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        https://salsa.debian.org/ruby-team/ruby-build/-/raw/%{salsa_commit}/debian/ruby-build.1.adoc

BuildRequires:  rubygem-asciidoctor

%if %{with check}
BuildRequires:  bats
%endif

# ruby-build can build various ruby interpreters from source, which in turn can
# require additional dependencies
Recommends:     bzip2
Recommends:     clang
Recommends:     gdbm-devel
Recommends:     java-headless
Recommends:     libffi-devel
Recommends:     libyaml-devel
Recommends:     llvm-devel
Recommends:     make
Recommends:     ncurses-devel
Recommends:     openssl-devel
Recommends:     patch
Recommends:     perl-File-Compare
Recommends:     perl-FindBin
Recommends:     readline-devel
Recommends:     ruby
Recommends:     rubygem-rake
Recommends:     rust
Recommends:     zlib-devel

%description
ruby-build is a command-line utility that makes it easy to install virtually
any version of Ruby, from source.

%package        rbenv
Summary:        rbenv plugin to compile and install Ruby
Requires:       ruby-build = %{version}-%{release}
Requires:       rbenv

%description    rbenv
This package contains a plugin for rbenv that provides the "rbenv install"
command.

%prep
%autosetup
cp -p %SOURCE1 .

%build
asciidoctor --backend manpage ruby-build.1.adoc

%install
PREFIX=%{buildroot}%{_prefix} ./install.sh
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 ruby-build.1

install -Ddpm0755 %{buildroot}%{_libdir}/rbenv/libexec
mv %{buildroot}%{_bindir}/rbenv-* %{buildroot}%{_libdir}/rbenv/libexec

%if %{with check}
%check
bats test
%endif

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%files rbenv
%{_libdir}/rbenv/libexec/*

%changelog
%autochangelog
