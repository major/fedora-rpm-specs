Name:             st
Version:          0.9.3
Release:          %autorelease
Summary:          A simple terminal implementation for X
%global           _stsourcedir %{_usrsrc}/%{name}-user-%{version}-%{release}
License:          MIT
URL:              http://%{name}.suckless.org/
Source0:          http://dl.suckless.org/%{name}/%{name}-%{version}.tar.gz
Source1:          %{name}.desktop
Source2:          %{name}-user
Source3:          %{name}-user.1
BuildRequires:    binutils
BuildRequires:    coreutils
BuildRequires:    gcc
BuildRequires:    desktop-file-utils
BuildRequires:    libX11-devel
BuildRequires:    libXext-devel
BuildRequires:    libXft-devel
BuildRequires:    make
BuildRequires:    sed
Requires:         font(liberationmono)
Requires:         ncurses-base
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description
A simple virtual terminal emulator for X which sucks less.

%package user
Summary:          Sources and tools for user configuration of st
License:          MIT
Requires:         %{name}%{?_isa} = %{version}-%{release}
Requires:         binutils
Requires:         coreutils
Requires:         findutils
Requires:         gcc
Requires:         libX11-devel
Requires:         libXext-devel
Requires:         libXft-devel
Requires:         make
Requires:         patch
Requires:         redhat-rpm-config
Requires(post):   %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

%description user
Source files for st and a launcher/builder wrapper script for
customized configurations.

%prep
%autosetup
# terminfo entries are provided by ncurses-base
sed -e "/tic .*st.info/d" -i Makefile

%build
%make_build CFLAGS="%{optflags}" LDFLAGS="%{?__global_ldflags}"

%install
%make_install PREFIX=%{_prefix}
mv %{buildroot}%{_bindir}/%{name}{,-fedora}
install -pm755 %{SOURCE2} %{buildroot}%{_bindir}/%{name}-user
install -Dpm644 %{SOURCE3} %{buildroot}%{_mandir}/man1/%{name}-user.1
for file in \
    %{buildroot}%{_bindir}/%{name}-user \
    %{buildroot}%{_mandir}/man1/%{name}-user.1; do
sed -i -e 's/VERSION/%{version}/' \
       -e 's/RELEASE/%{release}/' \
       ${file}
done

# Clean compilation artifacts before copying source files for st-user
make clean

mkdir -p %{buildroot}%{_stsourcedir}
install -pm644 * \
    %{buildroot}%{_stsourcedir}
touch %{buildroot}%{_bindir}/%{name}
chmod 0755 %{buildroot}%{_bindir}/%{name}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%check
# No test suite exists

%pre
[ -L %{_bindir}/%{name} ] || rm -f %{_bindir}/%{name}

%post
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-fedora 10

%postun
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-fedora
fi

%post user
%{_sbindir}/update-alternatives --install %{_bindir}/%{name} %{name} \
    %{_bindir}/%{name}-user 20

%postun user
if [ $1 -eq 0 ] ; then
    %{_sbindir}/update-alternatives --remove %{name} %{_bindir}/%{name}-user
fi

%files
%license LICENSE
%doc FAQ LEGACY README TODO %{name}.info
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}-fedora
%{_mandir}/man1/%{name}.*
%{_datadir}/applications/%{name}.desktop

%files user
%ghost %{_bindir}/%{name}
%{_bindir}/%{name}-user
%{_mandir}/man1/%{name}-user.*
%{_stsourcedir}

%changelog
%autochangelog
