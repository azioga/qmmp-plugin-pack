%define oname qmmp

Summary:	A set of extra plug-ins for Qmmp
Name:		qmmp-plugin-pack
Version:	1.1.1
Release:	1
Group:		Sound
License:	GPLv2+
Url:		http://qmmp.ylsoftware.com/plugins.php
Source0:	http://qmmp.ylsoftware.com/files/plugins/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	yasm
BuildRequires:	qt5-devel
BuildRequires: qt5-linguist
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(libmpg123)
BuildRequires:	pkgconfig(qmmp) >= %{version}
BuildRequires:	pkgconfig(qmmpui) >= %{version}
BuildRequires:	pkgconfig(taglib)
Suggests:	%{oname}-ffap = %{EVRD}
Suggests:	%{oname}-mpg123 = %{EVRD}


%description
Plug-ins for Qmmp from Qmmp Plug-in Pack:
 * FFap - enhanced Monkey's Audio (APE) decoder
   (24-bit samples and embedded cue support)
 * MPG123 - MPEG v1/2 layer1/2/3 decoder using of libmpg123 library
 * Simple Ui - simple user interface based on standard widgets set

%files

#----------------------------------------------------------------------------

%package -n %{oname}-ffap
Summary:	Qmmp FFap Input Plugin
Group:		Sound

%description -n %{oname}-ffap
This is the FFap Input Plugin for Qmmp (enhanced Monkey's Audio (APE) decoder,
24-bit samples and embedded cue support).

%files -n %{oname}-ffap
%doc AUTHORS COPYING ChangeLog.rus README README.RUS ChangeLog ChangeLog.svn
%{_libdir}/%{oname}/Input/libffap.so

#----------------------------------------------------------------------------

%package -n %{oname}-mpg123
Summary:	Qmmp MPG123 Input Plugin
Group:		Sound

%description -n %{oname}-mpg123
This is the MPG123 Input Plugin for Qmmp (MPEG v1/2 layer1/2/3 decoder
using of libmpg123 library).

%files -n %{oname}-mpg123
%doc AUTHORS COPYING ChangeLog.rus README README.RUS ChangeLog ChangeLog.svn
%{_libdir}/%{oname}/Input/libmpg123.so


#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build
