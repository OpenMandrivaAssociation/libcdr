%define api	0.0
%define major	0
%define libname %mklibname cdr %{api} %{major}
%define devname %mklibname cdr -d

Summary:	A library providing ability to interpret and import Corel Draw drawings
Name:		libcdr
Version:	0.0.14
Release:	6
Group:		System/Libraries
License:	GPLv2+ or LGPLv2+
Url:		http://www.freedesktop.org/wiki/Software/libcdr
Source0:	http://dev-www.libreoffice.org/src/%{name}-%{version}.tar.xz

BuildRequires:	doxygen
BuildRequires:	libwpd-devel
BuildRequires:	libwpg-devel
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(lcms2)
BuildRequires:	pkgconfig(zlib)

%description
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package tools
Summary:	Tools to transform Corel Draw drawings into other formats
Group:		Books/Howtos 

%description tools
Tools to transform Corel Draw drawings into other formats.
Currently supported: XHTML, raw.

%package -n %{libname}
Summary:	A library providing ability to interpret and import Corel Draw drawings
Group:		System/Libraries

%description -n %{libname}
Libcdr is library providing ability to interpret and import Corel Draw
drawings into various applications. You can find it being used in
libreoffice.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static
    
%make

%install
%makeinstall_std 
# these binaries do nothing currently
rm -f %{buildroot}/%{_bindir}/cmx2*

%files tools
%{_bindir}/cdr2raw
%{_bindir}/cdr2text

%files -n %{libname}
%{_libdir}/%{name}-%{api}.so.%{major}*

%files -n %{devname}
%doc AUTHORS ChangeLog COPYING.*
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/html
%{_includedir}/%{name}-%{api}
%{_libdir}/%{name}-%{api}.so
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_bindir}/cdr2xhtml

