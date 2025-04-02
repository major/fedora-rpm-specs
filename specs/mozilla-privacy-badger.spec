# common macros, yet to be defined. see:
# https://fedoraproject.org/wiki/User:Kalev/MozillaExtensionsDraft
%global moz_extensions %{_datadir}/mozilla/extensions

%global ext_id jid1-MnnxcxisBPnSXQ@jetpack

%global firefox_app_id \{ec8030f7-c20a-464f-9b0e-13a3a9e97384\}
%global firefox_inst_dir %{moz_extensions}/%{firefox_app_id}

Name:           mozilla-privacy-badger
Version:        2025.3.27
Release:        %autorelease
Summary:        Protects your privacy by blocking spying ads and invisible trackers
License:        Apache-2.0 AND GPL-3.0-or-later AND (GPL-3.0-or-later OR MPL-2.0) AND MIT AND OFL-1.1 AND LicenseRef-Fedora-Public-Domain AND CC-BY-SA-3.0
URL:            https://www.eff.org/privacybadger
Source0:        https://github.com/EFForg/privacybadger/archive/release-%{version}/privacybadger-%{version}.tar.gz
Source1:        %{name}.metainfo.xml
Requires:       mozilla-filesystem
BuildArch:      noarch
BuildRequires:  libappstream-glib
BuildRequires:  python3
BuildRequires:  zip
# lib/vendor/jquery-3.7.0.js
# https://jquery.com MIT
Provides:       bundled(js-jquery) = 3.7.0
# lib/vendor/jquery.smooth-scroll.js
# https://github.com/kswedberg/jquery-smooth-scroll MIT
Provides:       bundled(js-jquery-smooth-scroll) = 2.2.0
# lib/vendor/jquery-ui.custom/jquery-ui.min.js
# lib/vendor/jquery-ui.custom/jquery-ui.structure.min.css
# lib/vendor/jquery-ui.custom/jquery-ui.theme.min.css
# https://jqueryui.com MIT
Provides:       bundled(js-jquery-ui) = 1.13.2
# lib/vendor/jquery-ui-iconfont-2.3.2 CC-BY-SA 3.0
Provides:       bundled(js-jquery-ui-iconfont) = 2.3.2
# skin/fonts/Chunk.ttf
# https://www.fontsquirrel.com/fonts/chunkfive OFL
Provides:       bundled(fontsquirrel-chunk-five-fonts)
# skin/fonts/OpenSans-*.ttf
# http://www.google.com/fonts/specimen/Open+Sans ASL 2.0
Provides:       bundled(open-sans-fonts)
# lib/vendor/select2-4.0.11
# https://select2.github.io MIT
Provides:       bundled(js-select2) = 4.0.11
# lib/vendor/tooltipster-4.2.6
# http://iamceege.github.io/tooltipster/ MIT
Provides:       bundled(tooltipster) = 4.2.6
#
# lib/basedomain.js
# parts of original code from ipv6.js <https://github.com/beaugunderson/javascript-ipv6> MIT
#
# js/contentscripts/fingerprinting.js
# js/contentscripts/supercookie.js
# js/webrequest.js
# derived from https://github.com/ghostwords/chameleon MPL or GPLv3+
#
# js/contentscripts/socialwidgets.js
# js/socialwidgetloader.js
# skin/socialwidgets/socialwidgets.css
# Derived from ShareMeNot https://sharemenot.cs.washington.edu MIT
# 
# js/background.js
# js/options.js
# js/popup.js
# js/utils.js
# js/webrequest.js
# lib/i18n.js
# skin/options.html
# skin/popup.html
# derived from https://adblockplus.org/en/firefox GPLv3+
#
# js/firstparties/facebook.js
# adapted from https://github.com/mgziminsky/FacebookTrackingRemoval GPLv3+

%description
Privacy Badger is a browser add-on that stops advertisers and other third-party
trackers from secretly tracking where you go and what pages you look at on the
web. If an advertiser seems to be tracking you across multiple websites without
your permission, Privacy Badger automatically blocks that advertiser from
loading any more content in your browser. To the advertiser, it's like you
suddenly disappeared.

%prep
%setup -q -n privacybadger-release-%{version}

%build
# https://github.com/EFForg/privacybadger/blob/master/release-utils/make-eff-zip.sh

rm -rv src/tests src/data/dnt-policy.txt

# disable debug output
sed -i -e 's/\.DEBUG = true/.DEBUG = false/' src/js/bootstrap.js

# blank out locale descriptions to reduce package size
scripts/min_locales.py

# https://github.com/EFForg/privacybadger/blob/master/release-utils/firefox-release.sh
PATCHER=scripts/patch_manifest.py

mkdir pkg

$PATCHER src/manifest.json 'set' 'author' 'privacybadger-owner@eff.org'

$PATCHER src/manifest.json 'del' 'update_url'

rm -fv pkg/privacybadger-%{version}.zip
pushd src
zip -x pkg -v -r ../pkg/privacybadger-%{version}.zip ./*
popd

%install
install -Dpm644 pkg/privacybadger-%{version}.zip %{buildroot}%{firefox_inst_dir}/%{ext_id}.xpi
install -Dpm644 %{SOURCE1} %{buildroot}%{_metainfodir}/%{name}.metainfo.xml
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{name}.metainfo.xml

%files
%license LICENSE
%doc doc/Changelog
%doc doc/fixing-broken-sites.md
%doc doc/permissions.md
%doc doc/yellowlist-criteria.md
%dir %{firefox_inst_dir}
%{firefox_inst_dir}/%{ext_id}.xpi
%{_metainfodir}/%{name}.metainfo.xml

%changelog
%autochangelog
