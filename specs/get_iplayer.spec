Name:           get_iplayer
Version:        3.35
Release:        %autorelease
Summary:        Lists, records and streams BBC iPlayer TV and radio programmes

License:        GPL-3.0-or-later
URL:            https://github.com/get-iplayer/%{name}
Source:         %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Source:         get_iplayer.xml
Source:         get_iplayer.desktop

BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed

BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Encode::Locale)
BuildRequires:  perl(Env)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::stat)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Cookies)
BuildRequires:  perl(HTTP::Headers)
BuildRequires:  perl(integer)
BuildRequires:  perl(IO::Seekable)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(LWP::ConnCache)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(open)
BuildRequires:  perl(PerlIO::encoding)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(Text::ParseWords)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Unicode::Normalize)
BuildRequires:  perl(URI)

Requires:       /usr/bin/ffmpeg
Requires:       AtomicParsley
Requires:       perl-interpreter
Requires:       perl(Encode::Locale)
Requires:       perl(Mojolicious) >= 4.63

%description
get_iplayer is a tool for listing, recording and streaming BBC iPlayer
television and radio programmes, and other programmes via 3rd-party
plugins.

%prep
%autosetup

%build
# Generate the manpage
./get_iplayer --manpage=get_iplayer.1 || :

%install
install -Dpm0755 -t %{buildroot}%{_bindir} get_iplayer
install -Dpm0644 -t %{buildroot}%{_mandir}/man1 get_iplayer.1
touch options
install -Dpm0644 -t %{buildroot}%{_sysconfdir}/get_iplayer options
install -Dpm0644 -t %{buildroot}%{_datadir}/mime/packages %{SOURCE1}
desktop-file-install --dir=%{buildroot}/%{_datadir}/applications %{SOURCE2}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/get_iplayer
%{_mandir}/man1/get_iplayer.1*
%dir %{_sysconfdir}/get_iplayer
%config(noreplace) %{_sysconfdir}/get_iplayer/options
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/get_iplayer.xml

%changelog
%autochangelog
