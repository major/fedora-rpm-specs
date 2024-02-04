Name:          nyancat
Version:       1.5.2
Release:       %autorelease
Summary:       Nyancat rendered in your terminal

License:       NCSA
URL:           https://github.com/klange/nyancat
Source0:       %{URL}/archive/%{version}/%{name}-%{version}.tar.gz

# PATCHES FROM SOURCE GIT:

# Can now adjust image refresh rate
# Author: Tyler Cromwell <tyler@csh.rit.edu>
Patch0001: 00-0001-Can-now-adjust-image-refresh-rate.patch

# Converted spaces to tabs, and changed to setting a delay instead of a speed up amount
# Author: Tyler Cromwell <tyler@csh.rit.edu>
Patch0002: 01-0001-Converted-spaces-to-tabs-and-changed-to-setting-a-de.patch


BuildRequires: make
BuildRequires: gcc
BuildRequires: gawk

%description
Nyan Cat is the name of a YouTube video uploaded in April 2011, which became an
internet meme. The video merged a Japanese pop song with an animated cartoon
cat with a Pop-Tart for a torso, flying through space, and leaving a rainbow
trail behind it.


%prep
%autosetup -p1
awk '1;/\*\//{exit}' < src/nyancat.c > LICENSE


%build
%set_build_flags
make %{?_smp_mflags} nyancat


%install
mkdir -p %{buildroot}/%{_bindir}/
install -m 0755 src/nyancat %{buildroot}/%{_bindir}/
mkdir -p %{buildroot}/%{_mandir}/man1/
install -m 0644 nyancat.1 %{buildroot}/%{_mandir}/man1/


%files
%license LICENSE
%doc README.md
%{_bindir}/nyancat
%{_mandir}/man1/nyancat.1*


%changelog
%autochangelog
