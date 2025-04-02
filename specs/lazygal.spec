Name:           lazygal
Version:        0.10.11
Release:        %autorelease
Summary:        A static web gallery generator

License:        GPL-2.0-or-later AND MIT
URL:            https://sml.zincube.net/~niol/repositories.git/lazygal/about/
Source0:        https://sml.zincube.net/~niol/repositories.git/lazygal/snapshot/lazygal-%{version}.tar.bz2

BuildArch:      noarch

BuildRequires:  /usr/bin/ffmpeg
BuildRequires:  /usr/bin/ffprobe
BuildRequires:  gettext
BuildRequires:  js-jquery
BuildRequires:  pandoc
BuildRequires:  python3-devel
BuildRequires:  python3-gexiv2
BuildRequires:  python3dist(genshi)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(setuptools)
Recommends:     /usr/bin/ffmpeg
Recommends:     /usr/bin/ffprobe
Requires:       js-jquery
Requires:       python3-gexiv2
Requires:       python3dist(genshi)
Requires:       python3dist(pillow)
Provides:       bundled(jquery.tipTip.js) = 1.3
Provides:       bundled(respond.js) = 1.4.2
Provides:       bundled(jquery.colorbox.js) = 1.4.36
# still bundled JS in themes/
# inverted/SHARED_plugins.tjs TipTip 1.3 https://github.com/drewwilson/TipTip
# inverted/SHARED_respond.js https://github.com/scottjehl/Respond
# singlepage/SHARED_jquery.colorbox.js Colorbox v1.4.36 - http://www.jacklmoore.com/colorbox (available via npm)

%description
Lazygal is another static web gallery generator written in Python.
It can be summed up by the following features :
* Command line based (thus scriptable).
* Handles album updates.
* Presents all your pictures and videos and associated data.
* Makes browsing sharing pictures easy.
* Make customization easy.
* Does not change your original pictures directories (the source argument).

%prep
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
%{__python3} setup.py build_i18n
%{__python3} setup.py build_manpages

%install
%pyproject_install
install -dm755 %{buildroot}%{_mandir}/man{1,5}
install -pm644 man/lazygal.1 %{buildroot}%{_mandir}/man1/
install -pm644 man/lazygal.conf.5 %{buildroot}%{_mandir}/man5/
install -dm755 %{buildroot}%{_datadir}/locale
cp -pr build/mo/* %{buildroot}%{_datadir}/locale/

%find_lang %{name}
%pyproject_save_files lazygal

%check
%pyproject_check_import
%{py3_test_envvars} %{python3} -m unittest

%files -f %{name}.lang -f %{pyproject_files}
%license COPYING
%doc README.md TODO ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*

%changelog
%autochangelog
