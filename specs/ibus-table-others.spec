Name:       ibus-table-others
Version:    1.3.19
Release:    %autorelease
Summary:    Various tables for IBus-Table
License:    LGPL-2.1-or-later AND GPL-3.0-or-later AND WTFPL
URL:        http://github.com/moebiuscurve/ibus-table-others
Source0:    http://mfabian.fedorapeople.org/ibus-table-others/%{name}-%{version}.tar.gz
BuildArch:  noarch

Requires:         ibus-table
BuildRequires:    ibus-table-devel
BuildRequires: make

%description
The package contains various IBus-Tables which include languages of \
Latin-America, Europe, Southeast Asia, as well as math and other symbols

%package -n ibus-table-code
Requires:  ibus-table
Summary:   Ibus-Tables for Latex, CNS11643 & Emoticons
License:   LGPL-2.1-or-later

%description -n ibus-table-code
The package contains ibus-tables for Latex, CNS11643, Emoticons.

%package -n ibus-table-cyrillic
Requires:  ibus-table
Summary:   Ibus-Tables for Cyrillic
License:   LGPL-2.1-or-later

%description -n ibus-table-cyrillic
The Cyrillic rustrad & yawerty tables for IBus Table.

%package -n ibus-table-latin
Requires:  ibus-table
Summary:   Ibus-Tables for Latin
License:   LGPL-2.1-or-later AND GPL-3.0-or-later

%description -n ibus-table-latin
The Latin compose & ipa-x-sampa tables for Ibus-Table.

%package -n ibus-table-translit
Requires:  ibus-table
Summary:   Ibus-Tables for Russian Translit
License:   LGPL-2.1-or-later

%description -n ibus-table-translit
The Cyrillic translit & translit-ua tables for IBus-Table.

%package -n ibus-table-tv
Requires:  ibus-table
Summary:   Ibus-Tables for Thai and Viqr (Vietnamese)
License:   LGPL-2.1-or-later

%description -n ibus-table-tv
The Thai and Viqr (Vietnamese) tables for IBus-Table.

%package -n ibus-table-mathwriter
Requires:  ibus-table
Summary:  Ibus-Tables for Unicode mathematics symbols
License:  LGPL-2.1-or-later

%description -n ibus-table-mathwriter
The package contains table for writing Unicode mathematics symbols.

%package -n ibus-table-mongol
Requires:  ibus-table
Summary:  Ibus-Tables for Mongol Script
License:  WTFPL

%description -n ibus-table-mongol
The package contains a table for transliterating Latin Script to Mongol Script

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} NO_INDEX=true install
cd ${RPM_BUILD_ROOT}/%{_datadir}/ibus-table/tables/
%{_bindir}/ibus-table-createdb -i -n cns11643.db
%{_bindir}/ibus-table-createdb -i -n compose.db
%{_bindir}/ibus-table-createdb -i -n emoticon-table.db
%{_bindir}/ibus-table-createdb -i -n ipa-x-sampa.db
%{_bindir}/ibus-table-createdb -i -n latex.db
%{_bindir}/ibus-table-createdb -i -n rusle.db
%{_bindir}/ibus-table-createdb -i -n rustrad.db
%{_bindir}/ibus-table-createdb -i -n thai.db
%{_bindir}/ibus-table-createdb -i -n translit.db
%{_bindir}/ibus-table-createdb -i -n translit-ua.db
%{_bindir}/ibus-table-createdb -i -n viqr.db
%{_bindir}/ibus-table-createdb -i -n yawerty.db
%{_bindir}/ibus-table-createdb -i -n mathwriter-ibus.db

# Register as AppStream components to be visible in the software center
#
# NOTE: It would be *awesome* if these files were maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/emoticon-table.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>emoticon-table.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>LGPL-2.1-or-later</project_license>
  <name>Emoticon</name>
  <summary>Emoticon input method</summary>
  <description>
    <p>
      Emoticon is an input method that allows the user to enter pictorial representation
      of a facial or other expressions using characters—usually punctuation marks, numbers,
      and letters—to express a person's feelings, mood, or reaction, without needing to describe it in detail.
      This emoticon input method is mainly for Chinese users.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://code.google.com/p/ibus-table-emoticon/</url>
  <screenshots>
    <!-- FIXME: Needs an official up to date screenshot -->
    <screenshot type="default">
      <image>http://ibus-table-emoticon.googlecode.com/hg/screenshot.png</image>
      <caption><!-- Describe this screenshot in less than ~10 words --></caption>
    </screenshot>
  </screenshots>  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <languages>
    <lang percentage="100">zh_CN</lang>
    <lang percentage="100">zh_HK</lang>
    <lang percentage="100">zh_SG</lang>
    <lang percentage="100">zh_TW</lang>
  </languages>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/ipa-x-sampa.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>ipa-x-sampa.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>GPL-3.0-or-later</project_license>
  <name>International Phonetic Alphabet</name>
  <summary>IPA X-SAMPA input method</summary>
  <description>
    <p>
      International Phonetic Alphabet X-SAMPA is an input method.
      The Extended Speech Assessment Methods Phonetic Alphabet is a type of SAMPA
      developed by John C. Wells.
      It was designed to unify the individual SAMPA alphabets.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/mike-fabian/ibus-table-others</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/mathwriter-ibus.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>mathwriter-ibus.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>LGPL-2.1-or-later</project_license>
  <name>Mathwriter</name>
  <summary>Math symbols input method</summary>
  <description>
    <p>
      The input method is designed for entering mathematical symbols.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/mike-fabian/ibus-table-others</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/mongol_bichig.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<component type="inputmethod">
  <id>mongol_bichig.db</id>
  <metadata_license>CC0-1.0</metadata_license>
  <project_license>WTFPL</project_license>
  <name>Mongol Bichig</name>
  <summary>Transliteration to Mongol Script</summary>
  <description>
    <p>
      The input method is designed for transliterating Latin input to Mongol Script.
    </p>
    <p>
      Input methods are typing systems allowing users to input complex languages.
      They are necessary because these contain too many characters to simply be laid
      out on a traditional keyboard.
    </p>
  </description>
  <url type="homepage">https://github.com/mike-fabian/ibus-table-others</url>
  <url type="bugtracker">https://code.google.com/p/ibus/issues/list</url>
  <url type="help">https://code.google.com/p/ibus/wiki/FAQ</url>
  <update_contact><!-- upstream-contact_at_email.com --></update_contact>
</component>
EOF

%files
%doc AUTHORS COPYING README

%files -n ibus-table-code
%{_datadir}/appdata/emoticon-table.appdata.xml
%{_datadir}/ibus-table/tables/latex.db
%{_datadir}/ibus-table/tables/cns11643.db
%{_datadir}/ibus-table/tables/emoticon-table.db
%{_datadir}/ibus-table/icons/latex.svg
%{_datadir}/ibus-table/icons/cns11643.png
%{_datadir}/ibus-table/icons/ibus-emoticon.svg

%files -n ibus-table-cyrillic
%{_datadir}/ibus-table/tables/rusle.db
%{_datadir}/ibus-table/tables/rustrad.db
%{_datadir}/ibus-table/tables/yawerty.db
%{_datadir}/ibus-table/icons/rusle.png
%{_datadir}/ibus-table/icons/rustrad.png
%{_datadir}/ibus-table/icons/yawerty.png

%files -n ibus-table-latin
%{_datadir}/appdata/ipa-x-sampa.appdata.xml
%{_datadir}/ibus-table/tables/compose.db
%{_datadir}/ibus-table/tables/ipa-x-sampa.db
%{_datadir}/ibus-table/tables/hu-old-hungarian-rovas.db
%{_datadir}/ibus-table/icons/compose.svg
%{_datadir}/ibus-table/icons/ipa-x-sampa.svg
%{_datadir}/ibus-table/icons/hu-old-hungarian-rovas.svg

%files -n ibus-table-translit
%{_datadir}/ibus-table/tables/translit.db
%{_datadir}/ibus-table/tables/translit-ua.db
%{_datadir}/ibus-table/icons/translit.svg
%{_datadir}/ibus-table/icons/translit-ua.svg

%files -n ibus-table-tv
%{_datadir}/ibus-table/tables/telex.db
%{_datadir}/ibus-table/tables/thai.db
%{_datadir}/ibus-table/tables/viqr.db
%{_datadir}/ibus-table/tables/vni.db
%{_datadir}/ibus-table/icons/telex.png
%{_datadir}/ibus-table/icons/thai.png
%{_datadir}/ibus-table/icons/viqr.png
%{_datadir}/ibus-table/icons/vni.png

%files -n ibus-table-mathwriter
%{_datadir}/appdata/mathwriter-ibus.appdata.xml
%{_datadir}/ibus-table/tables/mathwriter-ibus.db
%{_datadir}/ibus-table/icons/mathwriter.png

%files -n ibus-table-mongol
%{_datadir}/appdata/mongol_bichig.appdata.xml
%{_datadir}/ibus-table/tables/mongol_bichig.db
%{_datadir}/ibus-table/icons/mongol_bichig.svg

%changelog
%autochangelog
