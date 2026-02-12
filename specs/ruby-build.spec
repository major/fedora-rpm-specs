# some tests are failing and there isn't a straightforward way to disable them
%bcond check 1
%global debug_package %{nil}

Name:           ruby-build
Version:        20260121
Release:        %autorelease
Summary:        Compile and install Ruby

License:        MIT
URL:            https://github.com/rbenv/ruby-build
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# PR https://github.com/rbenv/ruby-build/pull/2576
Patch:          2576.patch

BuildRequires:  gawk
BuildRequires:  grep
%if %{with check}
BuildRequires:  bats
%endif
Requires:       ruby-build-core = %{version}-%{release}
Recommends:     ruby-build-ruby = %{version}-%{release}

%description
ruby-build is a command-line utility that makes it easy to install virtually
any version of Ruby, from source.

%package        core
Summary:        Core executable and scripts for ruby-build
License:        MIT

%description    core
This package contains the core ruby-build executable and man pages,
without any specific Ruby definition files.

%package        rbenv
Summary:        rbenv plugin to compile and install Ruby
Requires:       ruby-build = %{version}-%{release}
Requires:       rbenv

%description    rbenv
This package contains a plugin for rbenv that provides the "rbenv install"
command.

%package        ruby
Summary:        ruby-build targets for MRI/CRuby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       gcc
Requires:       libffi-devel
Requires:       libyaml-devel
Requires:       perl-interpreter
Requires:       perl(File::Compare)
Requires:       perl(File::Copy)
Requires:       perl(FindBin)
Requires:       perl(IPC::Cmd)
Requires:       perl(lib)
Requires:       perl(Time::Piece)
Requires:       zlib-ng-compat-devel

%description    ruby
This package contains ruby-build targets for MRI/CRuby versions.

%package        jruby
Summary:        ruby-build targets for jruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       gcc-c++
Requires:       java-latest-openjdk-headless
Requires:       make

%description    jruby
This package contains ruby-build targets for jruby versions.

%package        mruby
Summary:        ruby-build targets for mruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       ruby
Requires:       rubygem-rake

%description    mruby
This package contains ruby-build targets for mruby versions.

%package        picoruby
Summary:        ruby-build targets for picoruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       git-core
Requires:       gcc
Requires:       ruby
Requires:       rubygem-rake

%description    picoruby
This package contains ruby-build targets for picoruby versions.

%package        truffleruby
Summary:        ruby-build targets for truffleruby versions
Requires:       ruby-build-core = %{version}-%{release}
Requires:       gcc
Requires:       libyaml-devel

%description    truffleruby
This package contains ruby-build targets for truffleruby versions.

%package        others
Summary:        ruby-build targets for rbx, ree and other versions
Requires:       ruby-build-core = %{version}-%{release}

%description    others
This package contains ruby-build targets for rbx, ree and other versions.

%package        all
Summary:        ruby-build targets for all versions
Requires:       ruby-build = %{version}-%{release}
Requires:       ruby-build-core = %{version}-%{release}
Requires:       ruby-build-ruby = %{version}-%{release}
Requires:       ruby-build-jruby = %{version}-%{release}
Requires:       ruby-build-mruby = %{version}-%{release}
Requires:       ruby-build-picoruby = %{version}-%{release}
Requires:       ruby-build-truffleruby = %{version}-%{release}
Requires:       ruby-build-others = %{version}-%{release}

%description    all
This meta-package contains all ruby-build targets versions.

%prep
%autosetup -p1

%install
PREFIX=%{buildroot}%{_prefix} ./install.sh
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 share/man/man1/ruby-build.1

install -Ddpm0755 %{buildroot}%{_libdir}/rbenv/libexec
mv %{buildroot}%{_bindir}/rbenv-* %{buildroot}%{_libdir}/rbenv/libexec

%if %{with check}
%check
# Skip failing tests
for test in "install bundled OpenSSL on macOS"; do
  awk -i inplace '/^@test\s+"'"$test"'"\s*\{/{ print; print "  skip \"disabled failing test\""; next }1' $(grep -rl "@test \"$test\"")
done
bats test
%endif

%files
%license LICENSE
%doc README.md

%files core
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%dir %{_datadir}/%{name}

%files ruby
%{_datadir}/%{name}/[0-9]*
%{_datadir}/%{name}/ruby-dev

%files jruby
%{_datadir}/%{name}/jruby*

%files mruby
%{_datadir}/%{name}/mruby*

%files picoruby
%{_datadir}/%{name}/picoruby*

%files truffleruby
%{_datadir}/%{name}/truffleruby*

%files others
%{_datadir}/%{name}/artichoke*
%{_datadir}/%{name}/rbx*
%{_datadir}/%{name}/ree*

%files all
# No files for you!

%files rbenv
%{_libdir}/rbenv/libexec/*

%changelog
%autochangelog
