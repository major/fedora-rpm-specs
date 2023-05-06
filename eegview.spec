# We do not use snapshot versioning even though we package from a commit hash
# because we believe this was intended to be the 1.1 release. See:
#   Please push a git tag for version 1.1
#   https://github.com/mmlabs-mindmaze/eegview/issues/11
%global commit de4b4c686982ab5e884d4cd13dc0c1140ce627b3

Name:           eegview
Version:        1.1
Release:        %autorelease
Summary:        Small program to display/record EEG signals

# Please clarify GPLv3 with a license statement
# https://github.com/mmlabs-mindmaze/eegview/issues/10
#   Without a license statement, we assume GPL-3.0-only rather than
#   GPL-3.0-or-later.
License:        GPL-3.0-only
URL:            https://opensource.mindmaze.com/projects/eegview/
Source0:        https://github.com/mmlabs-mindmaze/eegview/archive/%{commit}/eegview-%{commit}.tar.gz

# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch:    %{ix86}

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  eegdev-devel
BuildRequires:  mcpanel-devel
BuildRequires:  mmlib-devel
BuildRequires:  xdffileio-devel

BuildRequires:  desktop-file-utils

%description
eegview is a small program to display/record EEG signals. It is particularly
useful for setting up quickly the acquisition part of a offline protocol.


%prep
%autosetup -n eegview-%{commit}


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/eegview.desktop


%files
%license COPYING
%doc %{_docdir}/eegview/
%{_bindir}/eegview
%{_datadir}/applications/eegview.desktop
%{_mandir}/man1/eegview.1*


%changelog
%autochangelog
