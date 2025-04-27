Name: anyterm
Version: 1.2.3
Release: %autorelease
Summary: A web-based terminal emulator

License: GPL-2.0-or-later
URL: https://anyterm.org

# The source for this package was pulled from upstream's vcs.  Use the
# following commands to generate the tarball:
#  svn export http://svn.anyterm.org/anyterm/tags/releases/1.2/1.2.3 anyterm-1.2.3
#  tar -jcf anyterm-1.2.3.tar.xz anyterm-1.2.3
Source0: anyterm-1.2.3.tar.xz
Source1: anyterm-cmd
Source4: anyterm.conf
Source5: anyterm.service
Source6: anyterm.sysusers.conf
Source7: anyterm.tmpfiles.conf

# http://anyterm.org/1.1/install.html#secid2252601
Patch0: anyterm-change-url-prefix.patch
# svn diff --git -r 13873:18810
Patch1: anyterm-upstream-fixes-r18810.patch

BuildRequires: gcc-c++
BuildRequires: boost-devel
BuildRequires: zlib-devel
BuildRequires: systemd
BuildRequires: make
BuildRequires: systemd-rpm-macros
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%{?sysusers_requires_compat}


%package httpd
Summary: Httpd proxy configuration for anyterm
License: GPL-2.0-or-later
Requires: %{name} = %{version}-%{release}
Requires: httpd


%description
The Anyterm web-based terminal emulator, permits terminal and/or arbitrary
command access via http. The anyterm daemon can be configured to run any
arbitrary command, redirecting all standard input / output / error to
and from any javascript-enabled web browser in real time.

%description httpd
The httpd configuration necessary to proxy anyterm.

%prep
%setup -q
%patch -P0 -p0
%patch -P1 -p3

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
make %{?_smp_mflags} CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" OPTIMISE_FLAGS="$CXXFLAGS"
gzip anytermd.1

%install
install -Dp -m0755 anytermd %{buildroot}%{_sbindir}/anytermd
install -Dp -m0644 anytermd.1.gz %{buildroot}%{_mandir}/man1/anytermd.1.gz
install -Dp -m0755 %{SOURCE1} %{buildroot}%{_libexecdir}/%{name}/anyterm-cmd
install -Dp -m0644 %{SOURCE4} %{buildroot}%{_sysconfdir}/httpd/conf.d/anyterm.conf
install -Dp -m0644 %{SOURCE5} %{buildroot}%{_unitdir}/%{name}.service
install -Dp -m0644 %{SOURCE6} %{buildroot}%{_sysusersdir}/%{name}.conf
install -Dp -m0644 %{SOURCE7} %{buildroot}%{_tmpfilesdir}/%{name}.conf
install -Dp -m0644 browser/anyterm.css %{buildroot}%{_datadir}/%{name}/anyterm.css
install -Dp -m0644 browser/anyterm.html %{buildroot}%{_datadir}/%{name}/anyterm.html
install -Dp -m0644 browser/anyterm.js %{buildroot}%{_datadir}/%{name}/anyterm.js
install -Dp -m0644 browser/copy.gif %{buildroot}%{_datadir}/%{name}/copy.gif
install -Dp -m0644 browser/copy.png %{buildroot}%{_datadir}/%{name}/copy.png
install -Dp -m0644 browser/paste.gif %{buildroot}%{_datadir}/%{name}/paste.gif
install -Dp -m0644 browser/paste.png %{buildroot}%{_datadir}/%{name}/paste.png
install -Dp -m0644 browser/resizer.png %{buildroot}%{_datadir}/%{name}/resizer.png

%pre
%sysusers_create_compat %{SOURCE6}

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%files
%{_sbindir}/anytermd
%{_libexecdir}/anyterm/
%{_mandir}/man1/anytermd.1.gz
%{_datadir}/%{name}/
%{_unitdir}/%{name}.service
%ghost %attr(0755,%{name},%{name}) %dir %{_rundir}/%{name}
%{_tmpfilesdir}/%{name}.conf
%doc LICENSE
%{_sysusersdir}/%{name}.conf

%files httpd
%config(noreplace) %{_sysconfdir}/httpd/conf.d/anyterm.conf

%changelog
%autochangelog
