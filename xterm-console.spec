# Fedora spec initially based on upstream spec file from OBS:
# https://build.opensuse.org/package/view_file/devel:openQA:tested/xterm-console/xterm-console.spec
# License: MIT

%global github_owner    os-autoinst
%global github_name     xterm_console
%global github_version  1.1

Name:           xterm-console
Version:        %{github_version}
Release:        %{autorelease}
Summary:        A Linux vt console look-alike xterm wrapper
License:        MIT
URL:            https://github.com/%{github_owner}/%{github_name}
Source:         https://github.com/%{github_owner}/%{github_name}/archive/%{version}/%{github_name}-%{github_version}.tar.gz
BuildArch:      noarch
BuildRequires:  bdftopcf
# the original consolefonts:
BuildRequires:  kbd-misc
# For psf2bdf.pl
BuildRequires:  perl-interpreter

Requires:           xterm
Requires(post):     mkfontscale
Requires(postun):   mkfontscale

# svirt, eg. s390x, xen
Supplements:    os-autoinst

%description
xterm-console runs an xterm that tries to look as much as possible
like a console. It reads the current color configuration from the
kernel, and the package includes copies of the system console fonts
converted to the PCF format for xterm to use.

%prep
%autosetup -p1 -n %{github_name}-%{github_version}

%build
chmod +x ./psf2bdf.pl

for font in %{_prefix}/lib/kbd/consolefonts/*.psfu.gz; do
    fontname="${font##*/}"
    fontname="${fontname%.psfu.gz}"
    gunzip -c $font | ./psf2bdf.pl | sed -e "s,FONT \+-psf-,FONT ${fontname}," > "$fontname".bdf
done

for i in *.bdf; do
    bdftopcf "$i" | gzip -9 >"${i%.bdf}.pcf.gz"
done

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/X11/fonts/misc/

install -m 0755 xterm-console %{buildroot}%{_bindir}
install -m 0644 *.pcf.gz %{buildroot}%{_datadir}/X11/fonts/misc/

%post
mkfontdir %{_datadir}/X11/fonts/misc

%postun
if [ -d %{_datadir}/X11/fonts/misc ]; then
    mkfontdir %{_datadir}/X11/fonts/misc
fi

%files
%license LICENSE
%doc README.md
%{_bindir}/xterm-console
%dir %{_datadir}/X11/fonts
%dir %{_datadir}/X11/fonts/misc
%{_datadir}/X11/fonts/misc/*.pcf.gz

%changelog
%{autochangelog}
