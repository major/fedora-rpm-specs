Name:           mpdas
Version:        0.4.5
Release:        %autorelease
Summary:        An MPD audioscrobbling client


License:        BSD-3-Clause
URL:            http://50hz.ws/%{name}/
Source0:        %{url}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  libcurl-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  gcc-c++
Provides:       bundled(md5-deutsch)

%description
mpdas is a MPD AudioScrobbler client supporting the 2.0 protocol
specs. It is written in C++ and uses libmpd to retrieve the song
data from MPD and libcurl to post it to Last.fm


%prep
%setup -q

%build
export CONFIG="%{_sysconfdir}" PREFIX="%{buildroot}%{_prefix}" MANPREFIX="%{buildroot}%{_mandir}"
%set_build_flags
%make_build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix} %{buildroot}%{_mandir}/man1/ %{buildroot}%{_sysconfdir} %{buildroot}%{_bindir}

# Manually install them
install -m 0755 mpdas %{buildroot}%{_bindir}/mpdas
rm mpdas -f
install -m 0644 mpdas.1 %{buildroot}%{_mandir}/man1/mpdas.1

%files
%doc README mpdasrc.example
%license LICENSE
%{_mandir}/man1/mpdas.1*
%{_bindir}/mpdas

%changelog
%autochangelog
