Name:           rlwrap
Version:        0.46.1
Release:        %autorelease
Summary:        Wrapper for GNU readline

License:        GPLv2+
URL:            https://github.com/hanslub42/rlwrap
Source:         %{url}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  python3-rpm-macros
BuildRequires:  readline-devel

%description
rlwrap is a 'readline wrapper' that uses the GNU readline library to
allow the editing of keyboard input for any other command. Input
history is remembered across invocations, separately for each command;
history completion and search work as in bash and completion word
lists can be specified on the command line.


%prep
%autosetup -p1


%build
%configure
%make_build


%install
%make_install

# Fix shebangs to prevent bogus requirements
%{__sed} -r -i \
    -e 's|^#!.*perl$|#!%{__perl}|g' \
    -e 's|^#!.*python3$|#!%{__python3}|g' \
    $(find %{buildroot}%{_datadir}/%{name}/ -type f)


%check
make check


%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/rlwrap
%{_mandir}/*/rlwrap.*
%{_mandir}/man3/RlwrapFilter.*
%{_datadir}/rlwrap



%changelog
%autochangelog
