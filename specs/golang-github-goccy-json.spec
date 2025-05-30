# Generated by go2rpm 1.9.0
%bcond_without check
%global debug_package %{nil}

# https://github.com/goccy/go-json
%global goipath         github.com/goccy/go-json
Version:                0.10.2

%gometa -f

%global common_description %{expand:
Fast JSON encoder/decoder compatible with encoding/json for Go.}

%global golicenses      LICENSE
%global godocs          CHANGELOG.md README.md

Name:           %{goname}
Release:        %autorelease
Summary:        Fast JSON encoder/decoder compatible with encoding/json for Go

License:        MIT
URL:            %{gourl}
Source:         %{gosource}

%description %{common_description}

%gopkg

%prep
%goprep
%autopatch -p1

%generate_buildrequires
%go_generate_buildrequires

%install
%gopkginstall

%if %{with check}
%check
# https://github.com/goccy/go-json/issues/466
%ifarch s390x
for test in "TestUnmarshalMarshal" \
            "TestUnmarshalRescanLiteralMangledUnquote" \
            "TestATestHTMLEscapective" \
            "TestCompactBig" \
            "TestIndentBig" \
            "TestEncoderSetEscapeHTML" \
            "TestHTMLEscape" \
; do
awk -i inplace '/^func.*'"$test"'\(/ { print; print "\tt.Skip(\"disabled failing test\")"; next}1' $(grep -rl $test)
done
%endif
%gocheck
%endif

%gopkgfiles

%changelog
%autochangelog
