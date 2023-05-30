Name:           fedora-bookmarks
Version:        28
Release:        %autorelease
Summary:        Fedora bookmarks
License:        GFDL-1.1-or-later
URL:            http://fedoraproject.org/
# I had to strip the embedded icons out of the bookmarks file, because they are not 
# distributable under the GFDL. See https://bugzilla.redhat.com/show_bug.cgi?id=433471
Source0:        default-bookmarks.html
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Fedora.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks



%files
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
%autochangelog
